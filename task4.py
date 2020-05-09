import random
import os
import datetime
def login:
    welcome_options=input('Welcome Staff to Banking system App')
    while welcome_options == 'login':
        username_similar = input('Enter your username')
        password_similar = input('Enter your password')
        with open('staff.txt','r') as f:
            for line in f:
                info=line.split(',')
                username=str(info[0])
                password=str(info[1])
            if username_similar == username and password_similar == password:
                print('Login successful')
            else:
                print("Wrong details, try again")
                 new_session ='session.txt'
                session =open(new_session,'a+')
                session.write('you are logged in')
                session.write('\n')
                session.write(f'username:{username}')
                session.write('\n')
                session.write(f'password:{password}')
                session.close()
                f.close
                success = True
                while success == True:
                     print('Please chose an option''\n1. Create new bank account''\n2. Check Account Details''\n3. Logout')
        option = int(input('>:'))
        if option == 1:
            account_name = str(input('Account Name: ')).lower()
            opening_balance = float(input('Opening Balance: '))
            account_type = str(input('Account Type: ')).lower()
            account_email = input('Account email: ')
            account_number = ''.join(map(str, [random.randint(1,9) for a in range(0,10)]))
            customer_details = open('customer.txt', 'w+')
            customer_details.write('Account Name: %s\n' % account_name)
            customer_details.write('Opening Balance: %s\n' % opening_balance)
            customer_details.write('Account Type: %s\n' % account_type)
            customer_details.write('Account email: %s\n' % account_email)
            customer_details.write('Account Number: %s\n' % account_number)
            customer_details.close()

            print(f'Your Account Number is {account_number}')
            print('Please chose an option''\n1. Create new bank account''\n2. Check Account Details''\n3. Logout')
            option = int(input('>: '))

        if option == 2:
            input('input your Account Number: ')
            account_details = open('customer.txt', 'r')
            print(account_details.read())

            print('Please chose an option''\n1. Create new bank account''\n2. Check Account Details''\n3. Logout')
            option = int(input('>: '))

        if option == 3:
            session.close()
            os.remove("session.txt")
            print('Please choose an option''\n 1 Staff  details Login''\n 2 Close App')
            choice = int(input('>: '))


while choice == 2:
    print('Program Terminated''\nThank You and Good Bye')
    break