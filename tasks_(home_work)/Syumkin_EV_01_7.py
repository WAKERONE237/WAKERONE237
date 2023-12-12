"""
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
что задано положительное целое число). Протестируем функцию на файле article.txt со следующим содержимым:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела
"""

def read_last(lines, file):
    if not isinstance(lines, int) or lines <= 0:
        raise ValueError("Количество строк должно быть положительным целым числом")

    try:
        with open(file, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()

            for line in all_lines[-lines:]:
                print(line, end='')
    except FileNotFoundError:
        print(f"Файл {file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")



file_content = """Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела"""


with open('article.txt', 'w', encoding='utf-8') as file:
    file.write(file_content)


read_last(3, 'article.txt')

"""
Составьте программу - простейший редактор текстовых файлов. Алгоритм работы программы:

Программа предлагает ввести имя будущего файла. Записывает его, присваивая расширение .txt.
Программа предлагает записать строку в файл. При каждом нажатии кнопки ENTER происходит запись строки и переход на новую строчку.
Если строка пустая или спец. символ - программа сохраняет файл.
"""

def simple_text_editor():
    filename = input("Введите имя будущего файла (без расширения): ") + ".txt"

    with open(filename, 'w', encoding='utf-8') as file:
        while True:
            text_line = input("Введите строку для записи в файл (оставьте пустой или введите 'exit' для завершения): ")


            if text_line == "" or text_line.lower() == 'exit':
                print(f"Файл {filename} сохранён.")
                break


            file.write(text_line + "\n")

if __name__ == "__main__":
    simple_text_editor()
