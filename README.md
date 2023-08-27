# Bank Account App
This is a simple command-line bank account app written in Python that allows customers to create accounts, make deposits, and withdrawals. 

The app utilizes object-oriented programming principles to create and manage customer accounts.

# Features
Create a customer account with a random account number.

Display customer information including the account balance.

Make deposits to increase the account balance.

Perform withdrawals, with checks for sufficient funds.

# Usage
To use the Bank Account App, simply run the provided Python script bank_account_app.py in your preferred Python environment.

python bank_account_app.py

Upon running the script, the following functionalities are available:

Create Client Account: When you start the app, you will be prompted to enter your first name and last name.

An account will be created for you with a randomly generated account number.

Main Menu: After creating an account, you will be presented with a menu where you can choose various options.

    [D] Deposit: Allows you to deposit funds into your account.
    [W] Withdrawal: Allows you to withdraw funds from your account.
    [E] Exit: Exits the app.
    
Deposit: If you choose to deposit funds, you will be asked to enter the deposit amount. The amount will be added to your account balance.

Withdrawal: If you choose to make a withdrawal, you will be asked to enter the withdrawal amount. The app will check if you have sufficient funds before allowing the withdrawal.

Exit: To exit the app, choose the 'E' option from the menu. The app will display a thank you message.

# Code Structure
The code is structured into several classes and functions:

Person class: Represents a person with a first name and last name.

Customer class: Inherits from Person and represents a bank customer with additional attributes such as account number and account balance. It includes methods for deposit and withdrawal operations.

create_client() function: Prompts the user to enter their name and generates a random account number. It returns a Customer object.

start() function: Initiates the main loop of the app, allowing customers to perform banking operations.

# Note
This app is a basic example and does not include advanced security features, error handling, or persistent data storage. 

It is recommended to enhance the app with error handling for user inputs and consider security measures for handling sensitive information.

Feel free to modify and extend this app to suit your requirements.

Disclaimer: This app is provided for educational purposes and should not be used for real-world banking applications without proper security measures and testing.
