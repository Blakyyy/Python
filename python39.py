# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
import random
who = random.randint(0, 2)
candy = 228
while candy > 0:
    if who == 1:
        your_turn = int(input('Its your turn, please choose a number of candies you want to take from the box max(28): '))
        while your_turn > 28:
            your_turn = int(input('You can take maximum 28 candies, please choose antoher amount: '))
        candy = candy - your_turn
        if candy > 0:
            print(f'Candys left {candy}, its bot turn now')
            who = 0
        else: 
            print(f'You took the last {candy + your_turn} candies, you won')
            break
    elif who == 0:
        bot_turn = random.randint(1, 29)
        while bot_turn > candy:
            bot_turn = random.randint(1, 29)
        candy = candy - bot_turn
        print(f'Bot took {bot_turn} candies and {candy} candies left in the box ')
        if candy > 0:
            who = 1
        else:
            print(f'Bot took the last {candy + bot_turn} candies, he won')
            break



