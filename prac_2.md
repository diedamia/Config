## Задание 1
### Вывод служебной информации о пакете
```bash
pip show matplotlib
```
<img width = "500" src = "https://github.com/user-attachments/assets/5a1153fc-f68c-461f-a772-bf3be2e4520b">

### Получение пакета без менеджера пакетов, прямо из репозитория
```bash
git clone https://github.com/matplotlib/matplotlib.git
```
<img width = "500" src = "https://github.com/user-attachments/assets/e3e8b3c4-b13b-473e-82fb-a70e34d5e8ca">

## Задание 2
### Вывод служебной информации о пакете
```bash
npm info express
```
<img width = "800" src = "https://github.com/user-attachments/assets/4cdb35d3-9001-4faf-afdc-f67bc13e749d">

### Получение пакета без менеджера пакетов, прямо из репозитория
```bash
git clone https://github.com/expressjs/express.git
```
<img width = "500" src = "https://github.com/user-attachments/assets/c4e156d6-ee89-4c29-982e-150b19703249">

## Задание 3
### Изображение зависимостей matplotlib
```bash
echo "digraph G {\"matplotlib\" -> \"contourpy\"; \"matplotlib\" -> \"cycler\"; \"matplotlib\" -> \"fonttools\"; \"matplotlib\" -> \"kiwisolver\"; \"matplotlib\" -> \"numpy\"; \"matplotlib\" -> \"packaging\"; \"matplotlib\" -> \"pillow\"; \"matplotlib\" -> \"pyparsing\"; \"matplotlib\" -> \"python-dateutil\";}" | dot -Tpng -Nshape=rect -o pr_2_3.png
```
```bash
fim pr_2_3.png
```
<img width = "600" src = "https://github.com/user-attachments/assets/34254bc7-c307-4f6d-92c3-11f78717f961">

### Изображение зависимостей express
```bash
echo "digraph G {\"express\" -> \"body-parser\"; \"express\" -> \"cookie-parser\"; \"express\" -> \"serve-static\"; \"express\" -> \"debug\"; \"express\" -> \"express-session\";}" | dot -Tpng -Nshape=rect -o pr_2_3.png
```
```bash
fim pr_2_3.png
```
<img width = "600" src = "https://github.com/user-attachments/assets/9c14d8e6-0cad-4f46-b80f-1b66252b44a9">

## Задание 4
```bash
задания в процессе
```
<img src = "">

## Задание 5
```bash
example
```
<img src = "">

## Задание 6
```bash
example
```
<img src = "">

## Задание 7
```bash
example
```
<img src = "">
