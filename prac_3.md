# Задание 1 
```
{
  groups: [
    std.join("-", ["ИКБО", std.toString(i), "20"]) for i in std.range(1, 24)
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Иванов И.И."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Сидоров С.С."
    },
    {
      "age": 18,
      "group": "ИКБО-10-20",
      "name": "Карапетян В.С."
    },
  ],
  "subject": "Конфигурационное управление"
} 
```
<img src="https://github.com/user-attachments/assets/a81b489a-31fa-455c-91f9-098c1775468b">

# Задание 2
```
let generate = https://prelude.dhall-lang.org/List/generate
let makeUser = \(index : Natural) -> "ИКБО-${Natural/show (index + 1)}-20"
let user = Text

let makeStudent =
\(age: Natural)
-> \(group: Text)
-> \(name: Text)
-> {age, group, name}
in {
groups = generate 25 Text makeUser
,
students =
      [ makeStudent 19 "ИКБО-4-20" "Иванов И.И."
      , makeStudent 18 "ИКБО-5-20" "Петров П.П."
      , makeStudent 18 "ИКБО-5-20" "Сидоров С.С."
      , makeStudent 18 "ИКБО-10-23" "Карапетян В.С."
      ]
, 
subject = "Конфигурационное управление"
}
```
<img src="https://github.com/user-attachments/assets/65258e2f-c3d4-453f-85ca-e011f33960da">

# Задание 3
```
BNF = '''
  E = 0 | 1 | 0 E | 1 E
  '''
```
<img height=200 src="https://github.com/user-attachments/assets/f9056267-a57e-4f76-ab17-b10aec300f14">

# Задание 4
```
BNF = '''
  E = ( ) | { } | ( E ) | { E } | E E
  '''
```
<img height=200 src="https://github.com/user-attachments/assets/d9722d5b-c0a4-4465-9846-df0547d40e1c">

# Задание 5
```
BNF = '''
  E = x / y / E act E / ( E ) / ~ E
  act = & / |
  '''
```
<img height=200 src="https://github.com/user-attachments/assets/8a7098c7-6284-4ecd-84e9-7a0aa44d433e">
