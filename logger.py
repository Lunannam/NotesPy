from datetime import datetime as dt
from typing import List

def get_choice_logger(choise):
    time = dt.now().strftime('%D:%M:%H:%M')
    with open('log.log', 'a',encoding='utf-8') as file : 
            file.write('{};- user нажал цифру ; {}\n'
                .format(time, choise))

def add_note_logger(note):
    time = dt.now().strftime('%D:%M:%H:%M')
    with open('log.log', 'a',encoding='utf-8') as file : 
        file.write('{}; added_new_note; {}\n'
                .format(time, note))

def select_note_logger(key,value):
    time = dt.now().strftime('%D:%M:%H:%M')
    with open('log.log', 'a',encoding='utf-8') as file : 
        file.write('{}; select_note № {}\n'
                .format(time, key,value))


def search_note_logger(searched_note):
    time = dt.now().strftime('%D:%M:%H:%M')
    with open('log.log', 'a',encoding='utf-8') as file : 
        file.write('{}; search_note; {}\n'
                .format(time, searched_note))
