user_input = input('ведите пароль:')
line_counting = len(user_input)
# checking_numbers_or_letters = user_input.isdigit()
# print('Длина пароля:', line_counting)
if line_counting < 12:
	print('короткий')
else:
	print('длинный')



for letter in user_input:
	user_input = letter.isdigit()
	if user_input == False:
		print(letter,'- Буква')
	else:
		print(letter,'- Цифра')


def check_numbers_in_password(number):
	humber_found = False
	print('есть цифр')
	for numbers in letter:
		if number.number():
			number_found = True
			print('Нет цифр')
	return number_found
	
