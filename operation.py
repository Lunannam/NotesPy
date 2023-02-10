
import json
import csv
from typing import List



def read_csv():
    '''
    Чтение из файла csv
    '''
    note_list = []
    with open('data.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            line = ''.join(line)
            note_list.append(line)
        return note_list


def note_book_write_csv(note_book: List) -> None:
    '''
    Запись в csv фаил. Этот же метод добавляет заметку. На дозвпись в файл mode_type = 'а', на перезапись файла = 'w'
    '''
    with open('data.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerow(note_book)


def add_note_csv(note: List) -> None:
    '''
    Запись в csv фаил. Этот же метод добавляет заметки. На дозвпись в файл mode_type = 'а', на перезапись файла = 'w'
    '''
    with open('data.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow(note)


def search_note(searchstring: str) -> list:
    '''
    Поиск в записной книжке
    '''
    note_list = read_csv()
    searched_note = []
    for note in note_list:
        if searchstring in note:
            searched_note.append(note)
  
    return searched_note


def edit_note(searchstring: str, new_note: List) -> None:
    '''
    Редактирование. На вход метод принимает поисковую строку для заметки и измененную строку. 
    После перезаписываем файл с новыми измененниям
    '''
    delete_note(searchstring)
    add_note_csv(new_note)


def delete_note(searchstring: str) -> None:
    '''
    Ищем и удаляем заметку из списка. Перезаписываем файл
    '''
    note_list = read_csv()
    for note in note_list:
        if searchstring in note:
            note_list.remove(note)
    note_book_write_csv(note_list)


def write_json() -> None:
    '''
    Вызвать метод для первой записи в файле
    '''
    note_book = read_csv()
    with open('data.json', 'w', encoding='utf-8', newline='') as rf:
        json.dump(note_book, rf, ensure_ascii=False, indent=2)
