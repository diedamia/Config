import tkinter as tk
import os
import tarfile
import xml.etree.ElementTree as ET
import calendar
from datetime import datetime

from position import Position


class ShellEmulator:
    _ps1: str = "[{username}@{hostname}]$ "
    _command_input: tk.Text

    def __init__(self, config):
        self._cur_path = '/'
        self._window = tk.Tk()
        self._username = config['username']
        self._hostname = config['hostname']
        self._vfs_path = config['vfs_path']
        self._log_path = config['log_path']
        self._startup_script = config['startup_script']
        self._ps1 = self._ps1.format(username = self._username, hostname=self._hostname)
        self._cur_pos = Position(1,len(self._ps1))
        self._archive = tarfile.TarFile(self._vfs_path)

        self.configWindow()
        self._bindings()

    def run_startup_script(self, script_path):
        if os.path.exists(script_path):
            with open(script_path, 'r') as script_file:
                for line in script_file:
                    cmd = line.strip()
                    if cmd:
                        self._command_input.insert(tk.END, cmd + "\n")
                        self._execute()
  
    def run(self):
        self._pack()
        self.run_startup_script(self._startup_script)
        self._window.mainloop()


    def _print(self, str):
        self._command_input.insert(tk.END, str)

        if "\n" in str:
            self._cur_pos.add_line(str.count("\n") )

                      
    #Настройка окна приложения
    def configWindow(self):
        self._window.title("Shell Emulator")
        self._command_input = tk.Text(master=self._window)
        self._command_input.insert(tk.END, self._ps1)

    #Обработка Enter
    def _bindings(self):
        def handle_keypress(event):
            if event.keysym == "Return":
                self._execute()

        self._window.bind("<Key>", handle_keypress)
    
    #Размещение текстового поля в окне
    def _pack(self):
        self._command_input.pack()

    #Логирование
    def log_action(self, command):
        now = datetime.now()
        log_entry = ET.Element("entry")
        ET.SubElement(log_entry, "timestamp").text = now.strftime("%Y-%m-%d %H:%M:%S")
        ET.SubElement(log_entry, "user").text = self._username
        ET.SubElement(log_entry, "command").text = command

        # Создание или загрузка существующего лога
        if os.path.exists(self._log_path):
            tree = ET.parse(self._log_path)
            root = tree.getroot()
        else:
            root = ET.Element("log")
        
        root.append(log_entry)

        # Сохранение лога
        tree = ET.ElementTree(root)
        tree.write(self._log_path)

    #Считывание и обработка команд
    def _execute(self):
        cmd = self._command_input.get(self._cur_pos.to_str(), tk.END)[:-2]
        args = cmd.split()
        self.log_action(cmd)

        if (len(args) > 0):
            if args[0] == "ls":
                self._print(self.ls(args[1:]))
            elif args[0] == "cd":
                self._print(self.cd(args[1:]))
            elif args[0] == "exit":
                self.exit()
            elif args[0] == "cal":
                self._print(self.cal(args[1:]))
            elif args[0] == "pwd":
                self._print(self.pwd()+"\n")
            else:
                self._print("Неизвестная команда\n")

        self._print(self._ps1)
        self._cur_pos.add_line(1)

    def ls(self, args):
        if args:
            #абсолютный путь
            if args[0][0] == '/':
                path = args[0]
            else:
                #соединение пути с текущей директорией
                path = os.path.join(self._cur_path, args[0])

        else:
            #текущая директория
            path = self._cur_path

        file_set = set()
        for name in self._archive.getnames():
            name = '/' + name
            if name.startswith(path):
                name = name[len(path):].strip('/').split('/')[0]
                if name:
                    file_set.add(name)
        result = sorted(file_set)
        if result:
            return ('\n'.join(result) + '\n')
        return 'Директория не содержит файлы или не существует\n'
    
    def cd(self, args):
        if not args:
            return ''

        target_path = args[0]
        #Корневая директория
        if target_path == "/":
            self._cur_path = target_path
            return ''
        #Переход на родительскую директорию
        elif target_path == '..':
            if self._cur_path != '/':
                self._cur_path = os.path.dirname(self._cur_path)
            return ''
        #Формирование полного пути
        if target_path[0] == '/':
            path = target_path
        else:
            if not self._cur_path.endswith('/'):
                self._cur_path += "/"
            path = os.path.join(self._cur_path, target_path)

        for name in self._archive.getnames():
            name = '/' + name
            if (name.startswith(path + '/') and len(name) > len(path)):
                self._cur_path = path
                return ''
            
        return "Некорректный путь\n"

    def exit(self):
        self._window.destroy()
        exit(0)

    def pwd(self) :
        return self._cur_path

    def cal(self, args):
        cur_year = datetime.now().year
        cur_month = datetime.now().month
        if len(args) == 0:
            return calendar.month(cur_year, cur_month)
        elif len(args) == 1:
            year = int(args[0])
            return calendar.calendar(year)
        elif len(args) == 2:
            month = int(args[0])
            year = int(args[1])
            return calendar.month(year, month)
        else:
            return "Некорректные аргументы\n"