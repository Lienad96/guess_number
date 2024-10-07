from random import randint
number = randint(1,100)
print('Угадайте число от 1 до 100')

def  main():
    while True:
        guess_1 = int(input('Введите число: '))

        if guess_1 < number:
            print('Ваше число меньше того, что загадано.')
        if guess_1 > number:
            print('ваше число больше того, что загадано.')

        if guess_1 == number:
            break


main()


print('Отличная интуиция! Вы угадали число :')