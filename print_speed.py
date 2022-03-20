from time import *
from datetime import *
from colorama import *
import utils as U
init(autoreset=True)


# Главное тело - игра
def game():
	U.clear_screen()

	sec = 3   # Секунды для таймера
	wrong = 0 # Счетчик ошибок
	
	text_to_check = input('Введите текст, который будете набирать на скорость: ')

	print(f'\n{"-"*20}')
	sleep(0.5)
	print(f'Ваш текст для набора: {Fore.BLACK}{Back.WHITE}{text_to_check}\n')
	sleep(0.5)
	print(Fore.BLACK + Back.WHITE + 'Приготовьтесь\n')
	sleep(1)
	for i in range(sec):
		print(f'{sec}...')
		sec -= 1
		sleep(1)

	time_now = datetime.now() # Время начала ввода
	user_text = input('Ввод: ') # Текст, который вводит пользователь
	wrong = U.Wrong(1, text_to_check, user_text) # Вычисление кол-ва ошибок
	wrong_counter = U.Wrong(2, count = wrong) # Склонение слова 'ошибка'

	print(f'Вы набрали текст за {Fore.BLACK}{Back.WHITE}{datetime.now() - time_now}')
	print(wrong_counter)


# Выйти из игры
def quit():
	print('Возвращайтесь ещё!')
	return sys.exit()


# Начальное меню
def menu():
	U.clear_screen()

	print('ДАВАЙТЕ ПРОВЕРИМ ВАШУ СКОРОСТЬ ПЕЧАТИ!\n')

	options = { # Опции для выбора пользователя
	'1' : ('Начать', game),
	'0' : ('Выйти', quit)
	}
	U.print_options(options) # Вывести опции на экран

	choise = U.user_input('10')
	options[choise][1]()

	_ = input('\nНажмите ENTER, чтобы продолжить... ')

if __name__ == '__main__':
	while 1:
		menu()