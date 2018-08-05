class Client:
    def __init__(self, id, name, password, balance):
        self.id = id
        self.name = name
        self.password = password
        self.balance = int(float(balance) * 100)

    def update_balance(self, change):
        self.balance += change

    def change_password(self, new_password):
        self.password = new_password

    def __repr__(self):
        return '{ ID: %s, name: %s, password: %s, balance: %.2f }\n' % (self.id, self.name, self.password, self.balance / 100)
