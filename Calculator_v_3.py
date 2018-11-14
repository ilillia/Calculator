def output_function(entry_value):
    try:
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

        function_dictionary = {
        '+': plus_function(f_n,s_n),
        '-': minus_function(f_n,s_n),
        '*': multiply_function(f_n,s_n),
        '/': divide_function(f_n,s_n)}

        res = function_dictionary[oper]
        print('{} {} {} = {}'.format(f_n, oper, s_n, res))
        
    except (OverflowError, ZeroDivisionError, Exception) as error:
        print('Detected:', error, sep=' ')
        

def input_values():

    input_function = True

    while input_function :

        try :

            returned_values = {}

            first_number  = float(input('Enter First Number >>> '))
            type_of_operation  = input('Enter Base Function >>> ')

            if type_of_operation not in ('+' ,'-' ,'*' ,'/'):
                print('Error: unknown function')
                print('Try again')
                print()
                continue
            else:
                pass

            second_number  = float(input('Enter Second Number >>> '))

            returned_values['first_number'] = first_number
            returned_values['operation'] = type_of_operation
            returned_values['second_number'] = second_number

            input_function = False

        except (ValueError,Exception) as error :
            print('Error:', error, sep=' ')
            print('Try again')
            print()
            continue

    return returned_values

def main():
    list_of_operation = ('+' ,'-' ,'*' ,'/')

    print()
    print('Base functions :  +  ,  -  ,  * ')
    print()

    entry_value = input_values()

    print()
    print(entry_value)
    print()

    output_function(entry_value)

if __name__ == '__main__':
    main()
