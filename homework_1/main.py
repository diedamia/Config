import configparser

from app import ShellEmulator 

def main():
    config = configparser.ConfigParser()
    config.read("config.ini")
    emulator = ShellEmulator(config["settings"])
    emulator.run()

if __name__ == "__main__":
    main()