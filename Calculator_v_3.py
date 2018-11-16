from output import output_function
from input import input_values

def main():

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