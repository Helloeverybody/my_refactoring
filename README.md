## Сравнение результатов тестирования

На первом изображении представлены результаты профилирования отрефакторенного кода
![Alt-текст](filter_tests.png "тесты нового")

На втором изображении представлены результаты профилирования неотрефакторенного кода
![Alt-текст](old_filter_testd.png "тесты старого")

Как можно заметить, в старом файле код даже не выполнился из-за переполнения, а в новом выполнился, но более 9 секунд ушло на ввод данных
