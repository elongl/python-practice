import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def string_to_dict(client_string):
    props = client_string.split('\t')
    return {'id': props[0], 'name': props[1], 'password': props[2], 'balance': round(float(props[3]) * 100)}


def dict_to_string(client_dict):
    return "%s\t%s\t%s\t%.2f\n" % (client_dict['id'], client_dict['name'], client_dict['password'], client_dict['balance'] / 100)


clients_file = open('clients.txt', 'r')
clients_lines = clients_file.read().splitlines()
clients_file.close()
clients = {}
for client in clients_lines:
    client_dict = string_to_dict(client)
    clients[client_dict['id']] = client_dict

while True:
    print("Please insert your account's ID.")
    account_id = input()
    if account_id not in clients:
        clear()
        print("Invalid account ID.")
    else:
        break

clear()
while True:
    print("Please insert your account's password.")
    account_password = input()
    if account_password != clients[account_id]['password']:
        clear()
        print("Invalid account password.")
    else:
        break

user = clients[account_id]
clear()
while True:
    clear()
    print(f'Welcome {user["name"]}! Please choose your action.')
    print('1. Check Your Balance.\n2. Withdraw Funds.\n3. Deposit Funds.\n4. Change Password.\n-1. Exit')
    try:
        action_index = int(input())
        if action_index == -1:
            clients_file = open('clients.txt', 'w')
            stringy = map(dict_to_string, clients.values())
            clients_file.writelines(stringy)
            print(f'Thank you {user["name"]} for using our service. Bye bye.')
            break

        elif action_index == 1:
            print('Your balance is: %.2f' % (user['balance'] / 100))
            print('Press enter to return to the main menu.')
            input()

        elif action_index == 2:
            print('How much money would you like to withdraw?')
            amount = abs(float(input()))
            if user['balance'] - int(float(amount) * 100) >= 0:
                user['balance'] -= int(float(amount) * 100)
                print('You new balance is: %.2f' % (user['balance'] / 100))
            else:
                print('Insufficient funds. Please try again.')
            print('Press enter to return to the main menu.')
            input()

        elif action_index == 3:
            print('How much money would you like to deposit?')
            amount = abs(float(input()))
            user['balance'] += int(float(amount) * 100)
            print('You new balance is: %.2f' % (user['balance'] / 100))
            print('Press enter to return to the main menu.')
            input()

        elif action_index == 4:
            print('What would you like your new password to be?')
            new_password = input()
            user['password'] = new_password
            print('You new password has been assigned.')
            print('Press enter to return to the main menu.')
            input()

    except ValueError:
        print("Please make sure you're entering the correct values.")
        print('Press enter to return to the main menu.')
        input()
        continue
