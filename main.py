from random import randint

print('-' * 25)
print('-- Welcome to the BANK --')
print('-' * 25)
print('\n')


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Customer(Person):
    def __init__(self, first_name, last_name, account_number, account_balance=0):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.account_balance = account_balance

    def __str__(self):
        return f'Client: {self.first_name} {self.last_name}\nAccount: {self.account_number}\nAccount Balance: ${self.account_balance}'

    def deposit(self, amount_deposit):
        self.account_balance += amount_deposit
        print("Deposit Accepted")

    def withdrawal(self, amount_withdrawn):
        if self.account_balance >= amount_withdrawn:
            self.account_balance -= amount_withdrawn
            print("Withdraw Complete")
        else:
            print("Insufficient Funds")


def create_client():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    account_number = randint(10000, 99999)
    client1 = Customer(first_name, last_name, account_number)

    return client1


def start():
    my_customer = create_client()
    print(my_customer)

    menu_choice = 0

    while menu_choice != 'E':
        print('Please choose an option: ')
        print('''
        [D] - Deposit
        [W] - Withdrawal
        [E] - Exit ''')

        menu_choice = input()

        if menu_choice == 'D':
            dep_amount = int(input("Deposit amount: "))
            my_customer.deposit(dep_amount)

        elif menu_choice == 'W':
            with_amount = int(input("Withdrawal amount: "))
            my_customer.withdrawal(with_amount)

        print(my_customer)

    print("Thanks for using the Bank of Python!\nHave a nice day!")


start()