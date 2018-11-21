def output_function(entry_value):

	f_n = entry_value['first_number']
	s_n = entry_value['second_number']
	oper = entry_value['operation']

	from _4_executive_block import count_function
	
	try:
		count_function(f_n,s_n,oper)

	except Exception as error:
		print('Detected:', error, sep=' ')

	else:
		print('{} {} {} = {}'.format(f_n, oper, s_n, count_function(f_n,s_n,oper)))