def string_counter():
    with open('phonebook.txt') as phonebook:
        last_used_id = 0
        for i in phonebook:
            last_used_id = int(i.split('**')[0])
    return last_used_id


def create_note():
    with open('phonebook.txt', 'a+') as phonebook:
        id = string_counter() + 1
        last_name = input('Введи фамилию: ')
        first_name = input('Введи имя: ')
        phone_number = input('Введи номер телефона: ')
        comment = input('Введи комментарий: ')
        phonebook.write(
            f'\n{id}**{last_name}**{first_name}**{phone_number}**{comment}')


def delete_note():
    id_to_del = input('Введи id записи для удаления: ')
    temp = ''
    with open('phonebook.txt', 'r') as phonebook:
        for i in phonebook:
            if i.split('**')[0] != id_to_del:
                temp += i
    with open('phonebook.txt', 'w') as phonebook:
        phonebook.write(temp)
