
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


# def get_symbol(input_string: str) -> str:
#      '''
#      Проверка символа для действий
#      '''
#      while True:
#          try:
#              char = input(input_string)
#              if char not in '+-/*':
#                  print('Не правильно!')
#                  continue
#              return char
#  
#          except ValueError:
#              print('Это не то ...')
#  
 
def get_selection(input_string: str) -> int:
     '''
     Проверка числа для выбора результата
     '''
     while True:
         try:
             char = input(input_string)
             if char in '12345':
                 return int(char)
             print('Не правильно!')
             continue
         except ValueError:
             print('Это не то ...')
 
 
def get_date(input_string: str) -> str:
     '''
     Проверка строки "название", она не должна быть пустой и ограничена по колличеству символов,
     проверка выведет первую букву имени в верхнем регистре,
     остальные будут в нижнем
     '''
     while True:
         string = input(input_string)
         if len(string) < 50:
             if len(string) != 0:
                 if string[0].isalpha():
                     return string.title()
                 else:
                     print('Ведите краткое название заметки')
             elif len(string) == 0:
                 print('Это поле должно быть заполнено. Ведите краткое название заметки')  
         else: 
             print('вы ввели слишком много символов. Ведите краткое название заметки')
           
 
def get_title(input_string: str) -> str:
     '''
    Проверка строки "название", она не должна быть пустой и ограничена по колличеству символов,
    проверка выведет первую букву имени в верхнем регистре,
    остальные будут в нижнем
     '''
     while True:
         string = input(input_string)
         if len(string) < 17:
             if len(string) != 0:
                 if string[0].isalpha():
                     return string.title()
                 else:
                     print('Это поле должно быть заполнено. Ведите краткое название заметки')
             elif len(string) == 0:
                 return string    
         else: 
             print('вы ввели слишком много символов. Ведите краткое название заметки')
       
def get_note_number(input_string: str) -> str:
     '''
     Проверка строки "номер заметки" на числа и длинну 
     '''
 
     while True:
         try:
             num = input(input_string)
             if len(num) < 1000:
                 if len(num) != 0:
                     num = int(num)
                     return str(num)
                 elif len(num) == 0:
                     print('Это поле должно быть заполнено')  
             else: 
                 print('вы ввели слишком много символов')
         except ValueError:
             print('Это не то ...')
 

def get_comment(input_string: str) -> str:
    '''
    Проверка строки с комментарием на колличество символов
    '''
    while True:
            string = input(input_string)
            if len(string) < 100:
                return string 
            else: 
                print('вы ввели слишком много символов. Краткость - сестра таланта!')
        

def note_number(num: str) -> bool:
    '''
    Проверка номера заметки на совпадение в базе
    '''
    path = 'data.csv'
    with open(path, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=' ')
        for line in reader:
            for i in line:    
                if num in line:
                    print('заметка с таким номером уже существует, введите другой номер!')
                    return True
                else:
                    return False

