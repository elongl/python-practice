import os
from decimal import Decimal, InvalidOperation


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def line_to_client(client_line):
    client = client_line.split('\t')
    return {'name': client[1], 'password': client[2], 'balance': Decimal(client[3])}


def client_to_line(client_dict):
    id = client_dict[0]
    client = client_dict[1]
    return "%s\t%s\t%s\t%.2f\n" % (id, client['name'], client['password'], client['balance'])


with open('clients') as clients_file:
    clients_lines = clients_file.read().splitlines()
clients = {cl[:cl.find('\t')]: line_to_client(cl) for cl in clients_lines}


while True:
    print("Please insert your account's ID.")
    user_id = input()
    if user_id not in clients:
        clear()
        print("Invalid account ID.")
    else:
        break

clear()
while True:
    print("Please insert your account's password.")
    user_password = input()
    if user_password != clients[user_id]['password']:
        clear()
        print("Invalid account password.")
    else:
        break

user = clients[user_id]
clear()
while True:
    clear()
    print(f'Welcome {user["name"]}! Please choose your action.')
    print('1. Check Your Balance.\n2. Withdraw Funds.\n3. Deposit Funds.\n4. Change Password.\n-1. Exit')
    try:
        action_index = int(input())
        if action_index == -1:
            clients_lines = map(client_to_line, clients.items())
            with open('clients', 'w') as clients_file:
                clients_file.writelines(clients_lines)
            print(f'Thank you {user["name"]} for using our service. Bye bye!')
            break

        elif action_index == 1:
            print('Your balance is: %.2f' % user['balance'])
            print('Press enter to return to the main menu.')
            input()

        elif action_index == 2:
            print('How much money would you like to withdraw?')
            amount = abs(Decimal(input()))
            if user['balance'] - amount >= 0:
                user['balance'] -= amount
                print('You new balance is: %.2f' % user['balance'])
            else:
                print('Insufficient funds. Please try again.')
            print('Press enter to return to the main menu.')
            input()

        elif action_index == 3:
            print('How much money would you like to deposit?')
            amount = abs(Decimal(input()))
            user['balance'] += amount
            print('You new balance is: %.2f' % user['balance'])
            print('Press enter to return to the main menu.')
            input()

        elif action_index == 4:
            print('What would you like your new password to be?')
            new_password = input()
            user['password'] = new_password
            print('You new password has been assigned.')
            print('Press enter to return to the main menu.')
            input()

    except (InvalidOperation, ValueError):
        print("Please make sure you're entering the correct values.")
        print('Press enter to return to the main menu.')
        input()
        continue
