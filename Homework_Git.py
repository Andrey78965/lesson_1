def order(o):
    '''Функция проверяет является ли строка полинлромом или нет.

    :param o: str
    :return: возвращает True, если строка является палиндромом и False, если строка палиндромом не является.
    '''
    i = ''.join(reversed(o))
    if i == o:
        print(True)
    else:
        print(False)
order('лепсспел')
order('helloworld')


