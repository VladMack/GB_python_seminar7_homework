import file_writing
import output

def menu():
    print('Меню справочника:\n'
          '1. Добавить запись\n'
          '2. Удалить запись\n'
          '3. Вывести запись в строчку\n'
          '4. Вывести запись в столбик\n'
          '5. Вывести весь справочник в строчку\n'
          '6. Вывести весь справочник в столбик\n')
    point = 0
    while point < 1 or point > 6:
        point = int(input('Введи номер нужной функции: '))
        print()
    if point == 1:
        file_writing.create_note()
    if point == 2:
        file_writing.delete_note()
    if point == 3:
        output.print_note(', ')
    if point == 4:
        output.print_note('\n')
    if point == 5:
        output.print_phonebook(', ')
    if point == 6:
        output.print_phonebook('\n')
    whaiting = input()
