## Задача 1
```bash
cut -d: -f1 /etc/passwd | sort
```
<img height = 400 src="https://github.com/user-attachments/assets/92a2fb55-333d-45e7-8ed1-f760b2e6deb6">

## Задача 2
```bash
cat /etc/protocols | sort -nrk2 | head -n 5 | awk '{print $2, $1}'
```
<img src="https://github.com/user-attachments/assets/7a67127e-21f7-4462-81e9-49a6e74884fa">

## Задача 3
```bash
#!/bin/bash
text=$1
size=${#text}
echo -n "+"
for((i = 1; i <= size; i++))
do
echo -n "-"
done
echo "+"
echo "|$text|"
echo -n "+"
for((i = 1; i <= size; i++))
do
echo -n "-"
done
echo "+"
```
<img src="https://github.com/user-attachments/assets/2583b13d-2f89-41ff-ab4f-e6727e49f435">

## Задача 4
```bash
#!/bin/bash
file=$1
grep -o "[a-zA-Z_][a-zA-Z0-9_]*" "$file" | sort -u
```
<img src="https://github.com/user-attachments/assets/b63d30cc-f797-4c59-8f70-1f9934279e13
">

## Задача 5
```bash
#!/bin/bash
file=$1
sudo cp "$file" /usr/local/bin/
sudo chmod 755 /usr/local/bin/"$file"
```
<img src="https://github.com/user-attachments/assets/ed270c15-56b8-4ff0-bfb6-5f90d133b1fc">
<img src="https://github.com/user-attachments/assets/3e23943b-a50b-463f-a0a3-5ab4a188bac0">

## Задача 6
```bash
в процессе
```
