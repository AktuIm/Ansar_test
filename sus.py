
dictionary = {
    'cat': 'кот',
    'dog': 'собака',
    'book': 'книга',
    'house': 'дом',
    'car': 'машина'
}

def translate_word():
    word = input('Введите слово которое хотите перевести:')
    return dictionary[word]



def add_word():
    slowo = input('Введите слово которое хотите добавить(англ):')
    values = input('Введите значение, которое хотите добавить(русс):')
    dictionary[slowo] = values
    return 'Слово добавлено!'

def delete_word():
    goal = input('Введите слово, которое хотите удалить:')
    dictionary.pop(goal)
    return 'Слово удалено'

def main():
    while True:
        choose = int(input('Выберите номер действия:'))
        if choose == 1:
            print(translate_word())
        if choose == 2:
            print(add_word())
        if choose == 3:
            print(delete_word())
        if choose == 4:
            print('Вы вышли')
            break


if __name__ == '__main__':
    main()




