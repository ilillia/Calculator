def output_function(entry_value):

	f_n = entry_value['first_number']
	s_n = entry_value['second_number']
	oper = entry_value['operation']

	def plus_function(f_n,s_n):
		return f_n + s_n 
	def minus_function(f_n,s_n):
		return f_n - s_n
	def multiply_function(f_n,s_n):
		return f_n * s_n
	def divide_function(f_n,s_n):
		return f_n / s_n

	try:
		function_dictionary = {
		'+': plus_function(f_n,s_n),
		'-': minus_function(f_n,s_n),
		'*': multiply_function(f_n,s_n),
		'/': divide_function(f_n,s_n)}

	except Exception as error:
		print('Detected:', error, sep=' ')
	else:
		res = function_dictionary[oper]
		print('{} {} {} = {}'.format(f_n, oper, s_n, res))