def input_values():
    returned_values = {}
    while True :
        try :
            first_number  = float(input('Enter First Number >>> '))
            type_of_operation  = input('Enter Base Function >>> ')
            type_of_operation  = type_of_operation.replace(' ', '')

            if type_of_operation in ('+' ,'-' ,'*' ,'/'):
                second_number  = float(input('Enter Second Number >>> '))
            else:
                print('Error: unknown function')
                print('Try again')
                print()
                raise Exception('Unknown function') 

        except (ValueError,Exception) as error :
            print('Error:', error, sep=' ')
            print('Try again')
            print()
            continue

        else :
            returned_values['first_number'] = first_number
            returned_values['operation'] = type_of_operation
            returned_values['second_number'] = second_number
            return returned_values