
import csv




def get_number_int(input_string: str) -> int:
    '''
    Проверка целого числа
    '''
    while True:
        try:
            num = input(input_string)
            num = int(num)
            num = str(num) 
            return num
        except ValueError:
            print('Неверный ввод, введите число!')
 
def get_selection(input_string: str) -> int:
     '''
     Проверка числа для выбора результата
     '''
     while True:
         try:
             char = input(input_string)
             if char in '12345':
                 return int(char)
             print('Заметка уже существует, введите другое число!')
             continue
         except ValueError:
             print('Введите число ...')
 
 
def get_title(input_string: str) -> str:
     '''
     Проверка строки "название", она не должна быть пустой и ограничена по колличеству символов
     '''
     while True:
         string = input(input_string)
         if len(string) < 30:
             if len(string) != 0:
                     return string.title()           
             elif len(string) == 0:
                 print('Это поле должно быть заполнено. Ведите краткое название заметки')  
         else: 
             print('вы ввели слишком много символов. Ведите краткое название заметки')
           

def get_comment(input_string: str) -> str:
    '''
    Проверка строки с комментарием на колличество символов
    '''
    while True:
            string = input(input_string)
            if len(string) < 150:
                return string 
            else: 
                print('вы ввели слишком много символов. Краткость - сестра таланта!')
        

def note_number(num: str) -> bool:
    '''
    Проверка заметки на совпадение в базе
    '''
    path = 'data.csv'
    with open(path, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=' ')
        for line in reader:
            for i in line:    
                if i in line:
                    print('заметка уже существует, введите другое название!')
                    return True
                else:
                    return False

