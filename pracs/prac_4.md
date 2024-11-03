
# Задание 1 
<img src="https://github.com/user-attachments/assets/04f6b0e2-b97c-4b50-b3dc-192322a8f6a0">

# Задание 2
<img width=700px src="https://github.com/user-attachments/assets/f45b5160-6311-4beb-b1c5-3fb0a43b61c0">

# Задание 3

<img width=600px src="https://github.com/user-attachments/assets/a04ab177-06a1-49ff-8069-b858c93c6d5f">

<img width=600px src="https://github.com/user-attachments/assets/a5ef8356-1ca6-4d44-9197-aa0b50c23921">

### Coder1 получает актуальные данные с сервера. Добавляет в readme в раздел об авторах свою информацию и обновляет сервер.
<img width=600px src="https://github.com/user-attachments/assets/1f65ebeb-1f30-44cd-8882-f65a91f53f42">

### Coder2 пытается добавить в readme в раздел об авторах свою информацию
<img width=600px src="https://github.com/user-attachments/assets/94629674-aefc-48ea-ae82-389176212a9c">

### Получаем сообщение о конфликте
<img width=600px src="https://github.com/user-attachments/assets/c559664e-f9f9-42cd-8a57-715c63940eee">

### Разрешение конфликта и вывод лога коммитов
<img width=600px src="https://github.com/user-attachments/assets/b3164b02-8bc4-44ad-a925-e6510f88b992">

# Задание 4
```
import subprocess

def get_repo_contents(repo_path="."):
    process = subprocess.run(['git', 'rev-list', '--all'], capture_output=True, text=True, cwd=repo_path)
    objects = process.stdout.splitlines()
    for obj in objects:
        process = subprocess.run(['git', 'cat-file', '-p', obj], capture_output=True, text=True, cwd=repo_path)
        print(f"Объект: {obj}\nСодержимое:\n{process.stdout}\n---")

get_repo_contents()
```
<img src="https://github.com/user-attachments/assets/b233fb65-da50-43e1-81af-7185b3a7a992">
