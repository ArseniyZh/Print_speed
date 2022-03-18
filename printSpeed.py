from time import *
from datetime import *
from colorama import *
import os
from collections import Counter
init(autoreset=True)

def printSpeedCheck(text):
	sec = 3   # Секунды для таймера
	wrong = 0 # Счетчик ошибок
	wrongCount = '' # Грамотность склонения

	print(f'\n{"-"*20}')
	sleep(0.5)
	print(f'Ваш текст для набора: {Fore.BLACK}{Back.WHITE}{text}\n')
	sleep(0.5)
	print(Fore.BLACK + Back.WHITE + 'Приготовьтесь\n')
	sleep(1)

	for i in range(3):
		print(f'{sec}...')
		sec -= 1
		sleep(1)

	timeNow = datetime.now() # Время начала ввода
	textCheck = input('Ввод: ') # Текст, который вводит пользователь
	outSting = '' # Строка, показывающая ошибки пользователя (в разработке)
	wrong = Wrong(1, text, textCheck) # Вычисление кол-ва ошибок

	print(f'Вы набрали текст за {Fore.BLACK}{Back.GREEN}{datetime.now() - timeNow}')
	if wrong > 0: #Проверка на кол-во ошибок
		#Проверка на грамотность
		if wrong%10 == 1:
			wrongCount = 'ошибку'
		elif 1 < wrong%10 < 5:
			wrongCount = 'ошибки'
		elif wrong%10 == 0 or (5 < wrong%10 < 10):
			wrongCount = 'ошибок'

		print(f'Вы совершили {Fore.WHITE}{Back.RED}{wrong} {wrongCount}!')
	else:
		print(Fore.BLACK + Back.GREEN + 'ВЫ НЕ СОВЕРШИЛИ НИ ОДНОЙ ОШИБКИ!')

	#print(Wrong(2, text, textCheck))

	input('\nНажмите ENTER, чтобы продолжить...')
	main()


def Wrong(num, text, textCheck):
	if num == 1:
		wrong = len(Counter(text)) - (len(Counter(text) & Counter(textCheck))) # Вычисление кол-ва ошибок
		return wrong
	elif num == 2:
		pass
		# в разработке

def main():
	os.system('cls' if os.name=='nt' else 'clear')

	print('\nПроверим вашу скорость печати!')
	print('\nЕсли хотите выйти введите - 0')
	textFirst = input('Введите текст, который будете набирать на скорость: ')

	if textFirst == '0':
		print('\nПриходите еще!')
		return

	printSpeedCheck(textFirst)

			
main()