from random import randint


numb = randint(1,100)
print('Угадайте число от 1 до 100.')

while True:
    guess = int(input('Введите число:'))
    if guess < numb:
        print('Ваше число меньше загаданного.')
    elif guess > numb:
        print('Ваше число больше загаданного.')
    elif guess == numb:
        break
print('Отлично, вы угадали число: ',numb)
