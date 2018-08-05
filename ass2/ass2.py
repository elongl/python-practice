import os
from client import Client


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def string_to_object(client_string):
    return Client(*client_string.split('\t'))


clients_file = open('clients.txt', 'r')
clients_lines = clients_file.read().splitlines()
clients = {}
for client in clients_lines:
    client_object = string_to_object(client)
    clients[client_object.id] = client_object


while True:
    print("Please insert your account's ID.")
    account_id = input()
    if account_id not in clients:
        print("Invalid account id.")
        continue
    print("Please insert your account's password.")
    account_password = input()

    print('Please choose your action.')
    print('1. Check Your Balance.\n2. Withdraw Funds.\n3. Deposit Funds.\n4. Change Password.')
    action_index = input()
