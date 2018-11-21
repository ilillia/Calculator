from _2_input_block import input_values
from _3_output_block import output_function

def main():
    print('''
               ------------------------
              | Do you want to start ? |
               ------------------------
            ''')
    while True:
        
        preference = input('''          You have to choose between Yes and No 
                        >>>''')
        preference = preference.upper()
        preference = preference.replace(' ','')

        if preference == 'YES':
            print()
            print('Base functions :  +  ,  -  ,  * ')
            print()

            entry_value = input_values()

            print()
            print(entry_value)
            print()

            output_function(entry_value)

            print('''
               ---------------------------
              | Do you want to continue ? |
               ---------------------------
            ''')
            continue

        elif preference == 'NO':
            print('''
               -------------------------------
              | Program successfully finished |
               -------------------------------
            ''')
            break

        else:
            continue

if __name__ == '__main__':
    main()