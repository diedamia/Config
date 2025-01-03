## Визуализатор графа зависимостей
Согласно заданию варианта был разработан [инструмент командной строки для визуализации графа зависимостей](https://github.com/diedamia/Config/blob/main/homework_2/main.py), включая транзитивные зависимости, 
без использования сторонних программ или библиотек для получения зависимостей.

Зависимости определяются для [git-репозитория](https://github.com/diedamia/Config/tree/main/homework_2/test_repos). 

Для описания графа зависимостей используется [представление Graphviz](https://github.com/diedamia/Config/blob/main/homework_2/graph.dot). 

Визуализатор выводит результат в виде сообщения об успешном выполнении и сохраняет граф в [файле формата png](https://github.com/diedamia/Config/blob/main/homework_2/output.png).

Визуализатор выводит граф зависимостей для коммитов, в узлах которого содержатся хеш-значения.

Ключами командной строки задаются:

• Путь к программе для визуализации графов.

• Путь к анализируемому репозиторию.

• Путь к файлу с изображением графа зависимостей.

Пример команды [здесь](https://github.com/diedamia/Config/blob/main/homework_2/test_command.txt).

Все функции визуализатора зависимостей покрыты [тестами](https://github.com/diedamia/Config/blob/main/homework_2/tests.py).
