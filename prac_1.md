## Задача 1
```bash
cut -d: -f1 /etc/passwd | sort
```
<img height = 400 src="https://github.com/user-attachments/assets/92a2fb55-333d-45e7-8ed1-f760b2e6deb6">

## Задача 2
```bash
cat /etc/protocols | tail -n 5 | sort -nrk2 | awk '{print $2, $1}'
```
<img height = 100 src="https://github.com/user-attachments/assets/601b7212-1ed1-4bbc-bd70-91d99e635bd0">
