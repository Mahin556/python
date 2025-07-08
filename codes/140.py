
def calculate():
    num1,num2=input("Enter a number to sum:- ").split()
    print("Calculation....")

    print(f"Sum of {num1} and {num2} ==>> {int(num1)+int(num2)}")
    again()  # Prompt user again after calculation

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
        exit()
    else:
        again()

calculate()  # Start by calling calculate() once
