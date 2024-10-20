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
include "alldifferent.mzn";
var 0..9: d1;
var 0..9: d2;
var 0..9: d3;
var 0..9: d4;
var 0..9: d5;
var 0..9: d6;
constraint (d1 + d2 + d3) = (d4 + d5 + d6);
constraint all_different([d1, d2, d3, d4, d5, d6]);
solve minimize (d1 + d2 + d3);
```
<img src = "https://github.com/user-attachments/assets/835d96e2-c43e-4ec5-9015-5d96314a7658">

## Задание 5
```bash
enum PACKAGES = {
      root,
      menu_1_0_0, menu_1_1_0, menu_1_2_0, menu_1_3_0, menu_1_4_0, menu_1_5_0,
      dropdown_2_0_0, dropdown_2_1_0, dropdown_2_2_0, dropdown_2_3_0, dropdown_1_8_0,
      icons_1_0_0, icons_2_0_0
  };

array[PACKAGES] of var bool: depends;

constraint
      depends[root] == true;

constraint
      (depends[root] == true) -> (depends[menu_1_0_0] == true /\ depends[menu_1_5_0] == true /\ depends[icons_1_0_0] == true) /\
      (depends[menu_1_5_0] == true) -> (depends[dropdown_2_3_0] == true /\ depends[dropdown_2_0_0] == true) /\
      (depends[menu_1_4_0] == true) -> (depends[dropdown_2_3_0] == true /\ depends[dropdown_2_0_0] == true) /\
      (depends[menu_1_3_0] == true) -> (depends[dropdown_2_3_0] == true /\ depends[dropdown_2_0_0] == true) /\
      (depends[menu_1_2_0] == true) -> (depends[dropdown_2_3_0] == true /\ depends[dropdown_2_0_0] == true) /\
      (depends[menu_1_1_0] == true) -> (depends[dropdown_2_3_0] == true /\ depends[dropdown_2_0_0] == true) /\
      (depends[menu_1_0_0] == true) -> (depends[dropdown_1_8_0] == true) /\
      (depends[dropdown_2_3_0] == true) -> (depends[icons_2_0_0] == true) /\
      (depends[dropdown_2_2_0] == true) -> (depends[icons_2_0_0] == true) /\
      (depends[dropdown_2_1_0] == true) -> (depends[icons_2_0_0] == true) /\
      (depends[dropdown_2_0_0] == true) -> (depends[icons_2_0_0] == true);

var int: total_packages = sum([if depends[pkg] then 1 else 0 endif | pkg in PACKAGES]);

solve minimize total_packages;

output ["Total packages used: ", show(total_packages), "\nDependencies: ", show(depends)];
```
<img src = "https://github.com/user-attachments/assets/d6d89658-74d9-4360-b119-f44ed7263663">

## Задание 6
```bash
enum PACKAGES = {
      root,
      foo_1_0_0, foo_1_1_0,
      left_1_0_0, right_1_0_0,
      shared_1_0_0, shared_2_0_0,
      target_1_0_0, target_2_0_0
};

array[PACKAGES] of var bool: depends;

constraint
      depends[root] == true;

constraint
      (depends[root] == true) -> (depends[foo_1_0_0] == true /\ depends[target_2_0_0] == true) /\
      (depends[foo_1_1_0] == true) -> (depends[left_1_0_0] == true /\ depends[right_1_0_0] == true) /\
      (depends[left_1_0_0] == true) -> (depends[shared_1_0_0] == true /\ depends[shared_2_0_0] == true) /\
      (depends[right_1_0_0] == true) -> (depends[shared_1_0_0] == true) /\
      (depends[shared_1_0_0] == true) -> (depends[target_1_0_0] == true);

var int: total_packages = sum([if depends[pkg] then 1 else 0 endif | pkg in PACKAGES]);

solve minimize total_packages;

output ["Total packages used: ", show(total_packages), "\nDependencies: ", show(depends)];
```
<img src = "https://github.com/user-attachments/assets/2de38c6d-4a7c-49e3-bea4-2855b8966bf9">

## Задание 7
```bash
не решено
```
