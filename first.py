

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Your deposit must be greater than 0")
        else:
            print("Your deposit must be a number")
        
    return amount

deposit

def get_a_number_of_lines():

    while True:
        line = input("How many lines would you like to bet on 1 - 3 ? ")
        if line.isdigit():
            line = int(line)
            if 0 < line < 4:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
        
    return line
            

def main():
    balance = deposit()
    lines = get_a_number_of_lines()
    print(balance, lines)
main()
