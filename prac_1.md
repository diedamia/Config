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
#!/bin/bash
file_extention="${1##*.}"
first_line=$(head -n 1 $1)
if [[ "$file_extention" == "py" ]]; then
	if [[ ${first_line:0:1} == "#" ]]; then
		echo "Комметарий есть"
	else
		echo "Комментария нет"
	fi
elif [[ "$file_extention" == "c" ]] || [[ "$file_extention" == "js" ]]; then
	if [[ ${first_line:0:2} == "//" ]]; then
		echo "Комментарий есть"
	else
		echo "Комментария нет"
	fi
else
	echo "Файл имеет расширение, отличное от py, c и js"
fi
```
<img src="https://github.com/user-attachments/assets/bb964867-c94b-4f42-834f-dbd72dd64c8f">

## Задача 7
```bash
#!/bin/bash
t_file=$(mktemp)

find "$1" -type f -exec md5sum {} + | sort > "$t_file"

echo "Дубликаты файлов:"
awk '{
    if ($1 in seen) {
        print seen[$1] ", " $2
    } else {
        seen[$1] = $2
    }
}' "$t_file"

rm "$t_file"
```

<img src="https://github.com/user-attachments/assets/791f38bd-309e-479e-8c18-a2c6268a55e0">

## Задача 8
```bash
#!/bin/bash
find . -maxdepth 1 -name "*.$1" -print0| tar -cvzf archive_extention.tar.gz --null -T -
```

<img src="https://github.com/user-attachments/assets/ab6708ab-ff43-4d11-bbe3-961d1fe60e50">

## Задача 9
```bash
#!/bin/bash
sed 's/    /\t/g' "$1" > "$2"
```

<img src="https://github.com/user-attachments/assets/e513212f-b78a-4162-9ce6-258151844a5
">
<img height = 200 src="https://github.com/user-attachments/assets/1549b1f7-5fe2-4a7c-b348-2c8134b27c09">
<img height = 200 src="https://github.com/user-attachments/assets/f39806bc-32ae-408b-b602-4bce5acd1f0a">

## Задача 10
```bash
#!/bin/bash
find "$1" -type f -empty -name "*.txt"
```

<img src="https://github.com/user-attachments/assets/1b17691c-cbc7-416d-9c9d-d217651f79d2">
