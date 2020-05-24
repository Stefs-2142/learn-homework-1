def str_compare(str_1, str_2):
	""" Анализирует полученные аргументы """
	if type(str_1) == str and type(str_2) == str:
		if str_1 == str_2:
			return 1
		elif len(str_1) > len(str_2):
			return 2
		elif str_2 == 'learn':
			return 3
	else:
		return 0

def main():

	print(str_compare(12,'Python'))
	print(str_compare("learn",'learn'))
	print(str_compare("String",'str'))
	print(str_compare("",'learn'))

if __name__ == "__main__":
    	main()
