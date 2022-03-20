from collections import Counter
from colorama import *
import os


# Вывод опций на экран
def print_options(options):
	for shortcut, option in options.items():
		print(f'({shortcut}) {option[0]}')


# Ввод пользователя и проверка ввода на корректность по переданным опциям
def user_input(options):
	choise = input('\nВыберите вариант действий: ')

	while not choise in options:
		print('Недопустимый вариант')
		choise = input('Выберите вариант действий: ')
	return choise


# Очистка экрана
def clear_screen():
	clear = 'cls' if os.name == 'nt' else 'clear'
	os.system(clear)


def Wrong(num, text_to_check = None, user_text = None, count = None):
	if num == 1: # Возврощает количество ошибок
		wrong = Counter(text_to_check) - (Counter(text_to_check) & Counter(user_text)) # Вычисление кол-ва ошибок
		return sum(wrong.values())

	elif num == 2: # Возвращает количество ошибок и склонение слова 'ошибка'
		if count > 0: #Проверка на кол-во ошибок
			#Проверка на грамотность
			if count%10 == 1:
				wrong_word = 'ошибку'
			elif 1 < count%10 < 5:
				wrong_word = 'ошибки'
			elif count%10 == 0 or (5 < wrong%10 < 10):
				wrong_word = 'ошибок'

			return (f'Вы совершили {Fore.WHITE}{Back.RED}{count} {wrong_word}!')
		else:
			return (f'{Fore.BLACK}{Back.GREEN}ВЫ НЕ СОВЕРШИЛИ НИ ОДНОЙ ОШИБКИ!')