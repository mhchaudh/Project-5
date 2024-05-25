from getpass import getpass

#pre-defined dictionary with user-names, passwords and balance
accounts = {'admin' : ['2901'],
            'user1' : ['1234', 3000],
            'user2' : ['7008', 4000],
            'user3' : ['9876', 5000]}

#function that formats and prints a message given as param
def print_message(message):
    border = '=' * 50
    print(border)
    print('{:*^50s}'.format(message))
    print(border)
    print()

#takes care of logging the user into his account by entering correct username
#and password
def login(acc):
    users = list(acc.keys())
    while True:
        print("Please enter username and password.")
        user = input("Enter Username: ").lower()
        if user in users:
            count = 0
            actual_password = acc[user][0]
            while count < 3:
                password = getpass("Enter Pin: ")
                count += 1
                if password == actual_password:
                    print_message(' SUCCESSFULLY LOGGED IN. ')
                    return user
                else:
                    print_message(' INCORRECT PIN. TRY AGAIN! ')
            else:
                print_message(' INCORRECT PIN ENTERED 3 TIMES. EXITING... ')
                return ''
        else:
            print_message(' INVALID USERNAME ')

#checks the balance of the account given as a parameter
def check_balance(user, acc):
    print()
    print(user, 'Account Balance:', acc[user][1])

#increases the balance of the given account by an amount given from input
def deposit_funds(user, acc):
    while True:
        funds = input('Enter funds to deposit: ')
        try:
            funds = int(funds)
            break
        except ValueError:
            print_message(' Invalid Input. Try Again! ')
    balance = acc[user][1] + funds
    acc[user][1] = balance
    print(funds, 'deposited.')
    print('New balance:', balance)
    return acc

#decreases the balance of the given account by an amount given from input
def withdraw_funds(user, acc):
    while True:
        funds = input('Enter funds to withdraw: ')
        try:
            funds = int(funds)
            break
        except ValueError:
            print_message(' Invalid Input. Try Again! ')
    balance = acc[user][1] - funds
    acc[user][1] = balance
    print(funds, 'withdrawn.')
    print('New balance:', balance)
    return acc

#changes the pin of the given account
def change_pin(user, acc):
    old_password = acc[user][0]
    count =  0
    while count < 3:
        temp = getpass('Enter old pin: ')
        count += 1
        if temp == old_password:
            while True:
                new_password = getpass('Enter new pin: ')
                if len(new_password) != 4:
                    print_message(' MAKE SURE PIN IS 4 DIGITS! ')
                    continue
                confirmation = getpass('Confirm new pin: ')
                if new_password == confirmation:
                    print_message(' YOUR PIN IS CHANGED. ')
                    acc[user][0] = new_password
                    return acc
                else:
                    print_message(" PINS DON'T MATCH. TRY AGAIN! ")
        else:
            print_message(' OLD PIN IS INCORRECT. TRY AGAIN! ')
    else:
        print_message(' INCORRECT PIN ENTERED 3 TIMES. EXITING... ')
        return acc

#shows all the users in the system
def view_users(acc):
    print('=' * 20)
    print('|| USERNAME       ||')
    print('=' * 20)
    users = list(acc.keys())
    for user in users:
        print('|| {:<14s} ||'.format(user))
    print('=' * 20)
    print()

#adds a user to the system
def add_user(acc):
    print('Please enter username and password of the new user.')
    username = input('Enter username: ')
    while True:
        password = getpass('Enter pin: ')
        if len(password) != 4:
            print_message(' MAKE SURE PIN IS 4 DIGITS! ')
            continue
        confirmation = getpass('Confirm pin: ')
        if password == confirmation:
            while True:
                balance = input('Enter balance: ')
                try:
                    balance = int(balance)
                    break
                except ValueError:
                    print_message(' Invalid Input. Try Again! ')
            acc[username] = [password, balance]
            print_message(' NEW USER CREATED. ')
            return acc
        else:
            print_message(" PINS DON'T MATCH. TRY AGAIN! ")

#removes a user from the system
def remove_user(acc):
    view_users(acc)
    users = list(acc.keys())
    while True:
        user = input("Enter user to remove: ").lower()
        if user == 'admin':
            print_message(' ADMIN CANNOT BE REMOVED ')
            return acc
        if user in users:
            count = 0
            actual_password = acc[user][0]
            while count < 3:
                password = getpass("Enter Pin: ")
                count += 1
                if password == actual_password:
                    while True:
                        temp = input('Are you sure you want to remove {}? (Y/N) '.format(user)).lower()
                        if temp == 'y':
                            del acc[user]
                            print_message(' {} DELETED '.format(user))
                            return acc
                        elif temp == 'n':
                            return acc
                        else:
                            print_message(' PLEASE ENTER (Y) OR (N) ')
                else:
                    print_message(' INCORRECT PIN. TRY AGAIN! ')
            else:
                print_message(' INCORRECT PIN ENTERED 3 TIMES. EXITING... ')
                return acc
        else:
            print_message(' INVALID USERNAME ')

#called when a guest logs in
def guest():
    global accounts
    while True:
        print()
        print('1. Check account balance.')
        print('2. Deposit funds.')
        print('3. Withdraw funds.')
        print('4. Change ATM pin.')
        print('5. Log out')
        print('6. Exit')
        choice = input('Enter choice: ')
        if choice not in '123456':
            print_message(' INVALID CHOICE ENTERED. TRY AGAIN! ')
            continue
        else:
            if choice == '1':
                check_balance(user, accounts)
                inp = input('Press enter to continue.')
            elif choice == '2':
                accounts = deposit_funds(user, accounts)
                inp = input('Press enter to continue.')
            elif choice == '3':
                accounts = withdraw_funds(user, accounts)
                inp = input('Press enter to continue.')
            elif choice == '4':
                accounts = change_pin(user, accounts)
                inp = input('Press enter to continue.')
            elif choice == '5':
                start(accounts)
                break
            elif choice == '6':
                break

#called when an admin logs in
def admin():
    global accounts
    while True:
        print()
        print('1. View users.')
        print('2. Add user.')
        print('3. Remove user.')
        print('4. Log out')
        print('5. Exit')
        choice = input('Enter choice: ')
        if choice not in '12345':
            print_message(' INVALID CHOICE ENTERED. TRY AGAIN! ')
            continue
        else:
            if choice == '1':
                view_users(accounts)
                inp = input('Press enter to continue.')
            elif choice == '2':
                accounts = add_user(accounts)
                view_users(accounts)
                inp = input('Press enter to continue.')
            elif choice == '3':
                accounts = remove_user(accounts)
                inp = input('Press enter to continue.')
            elif choice == '4':
                start(accounts)
                break
            elif choice == '5':
                break

def start(acc):
    global user
    user = login(acc)
    if user != '':
        if user == 'admin':
            admin()
        else:
            guest()

start(accounts)
