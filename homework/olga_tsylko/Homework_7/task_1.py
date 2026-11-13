my_numb = 1

while True:
    user_numb = int(input('Введите любое число '))
    if user_numb == my_numb:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')
