import datetime as dt
import checks as ch
from colorama import Fore, Back, Style 
import logger as log
from datetime import datetime as dt


def greetings_user():
    '''
    Приветсвует пользователя
    '''
    print(f'{Fore.YELLOW + Style.BRIGHT}Добро пожаловать в записную книжку  {Style.RESET_ALL}')
    
def farewell_user():
    '''
    Прощание с пользователем
    '''
    print(f'{Fore.YELLOW + Style.BRIGHT}До новых встреч {Style.RESET_ALL}')


def view_data(lst_input: list) -> str: #показать заметки
    '''
    Вывод информации пользователю
    '''
    print(f'\n{Fore.YELLOW + Style.BRIGHT}      <Ваши заметки> ↓ ')
    for line in lst_input:
        print(line)

def get_note(): 
    print(f'{Fore.YELLOW + Style.BRIGHT}Введите информацию  ↓ {Style.RESET_ALL}')


def add_note(): #добавить зaметку
    note = []
    print(Fore.CYAN + Style.BRIGHT)
    text = dt.now().strftime('%D')
    note.append(text)
    text = id
    note.append(text)
    # text = ch.get_note_number(f'{Fore.CYAN + Style.BRIGHT}-> номер заметки: {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    # note.append(text)
    
    text = ch.get_title(f'{Fore.CYAN + Style.BRIGHT}-> название : {Fore.LIGHTGREEN_EX + Style.BRIGHT} ')
    
    note.append(text + ' ')
    text = ch.get_comment(f'{Fore.CYAN + Style.BRIGHT}-> описание : {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
 
    note.append(text + ' ')
    print(f'\n{Fore.GREEN} заметка успешно добавлена {Style.RESET_ALL}')
    print(Style.RESET_ALL)
    log.add_note_logger(note)
    return note


def get_choice(input_string: str) -> str:
    '''
    Ввод выбора действия пользователя

    '''
    choise = ch.get_selection(input_string)
    log.get_choice_logger(choise)
    return choise

def get_action(input_string: str) -> str:
    '''
    Ввод выбора действия пользователя

    '''
    return input(input_string)    


def show_menu()-> None:
    return ('\n'
      f'{Fore.YELLOW + Style.BRIGHT}Выберите нужное действие: ↓{Style.RESET_ALL}\n'
      f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}' 
      ' 1 - <добавление новой заметки> \n'
      ' 2 - <поиск заметки> \n'
      ' 3 - <просмотр заметок> \n'
      ' 4 - <выход> \n'
      f' ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
    
    
def search_note_user():
    print(get_action(f'{Fore.YELLOW + Style.BRIGHT}Введите значение для поиска ->: {Fore.LIGHTGREEN_EX + Style.BRIGHT}'))
    print(Style.RESET_ALL) 

def menu_search()-> None:
    '''
    Меню функции поиска
    '''
    return ('\n'
      f'{Fore.YELLOW + Style.BRIGHT}Выберите нужное действие: ↓{Style.RESET_ALL}\n'
      f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}' 
      ' 1 -  <Редактировать > \n'
      ' 2 - <Удалить > \n'
      ' 3 -  <Выйти в главное меню> \n'
      f' ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
 
def edit_user_note(searchstring: str) -> None:
    print(get_action(f'{Fore.YELLOW + Style.BRIGHT}Введите обновленные данные  {searchstring} ↓ {Fore.LIGHTGREEN_EX + Style.BRIGHT}'))
    print(Style.RESET_ALL)
    
def delete_user_note(searchstring: str) -> None:
    print(get_action(f'{Fore.YELLOW + Style.BRIGHT} заметка удалена  {searchstring} ↓ {Fore.LIGHTGREEN_EX + Style.BRIGHT}'))
    print(Style.RESET_ALL)