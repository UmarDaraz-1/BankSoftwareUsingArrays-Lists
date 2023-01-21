import array as arr
import random

accounts = arr.array('i', [])

def create_account():
    account_number = random.randint(1000, 9999)
    
    if account_number in accounts:
        create_account()
    else:
        accounts.append(account_number)
        print("Your account number is: {}".format(account_number))


def deposit(account_number, amount):
    if account_number in accounts:
        print("Deposited ${} in account number {}".format(amount, account_number))
    else:
        print("Invalid account number")


def withdraw(account_number, amount):
    if account_number in accounts:
        print("Withdrew ${} from account number {}".format(amount, account_number))
    else:
        print("Invalid account number")


def check_balance(account_number):
    if account_number in accounts:
        print("Your balance is $0")
    else:
        print("Invalid account number")

input_value = int(input("1: Create Account \n2: Deposit \n3: Withdraw \n4: Check BankBalance\n"))


if input_value == 1:
    create_account()

elif input_value == 2:
    check_balance()
            
elif input_value == 3:
    deposit()


elif input_value == 3:
    withdraw()

else:
    print("Please Enter a valid input.")
