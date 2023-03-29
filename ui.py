import Note

def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("""\nВыберите действие:\n
        1 - Показать все записи
        2 - Создание  заметки
        3 - Удаление заметки
        4 - Редактирование заметки
        5 - Выборка заметок по дате
        6 - Показать заметку по id
        0 - Выход\n
        Введите номер функции: """)


def check_len_text_input(text, n):
    while len(text) < n:
        print(f'Текст должен содержать хотя бы {n} символ\n')
        text = input('Введите тескт: ')
    else:
        return text


def exiting_app():
    print("Приложение не активно")