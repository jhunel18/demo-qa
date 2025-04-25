class ATM:
    def __init__(self, user_data):
        self.user_data = user_data
        self.current_user = None

    def login(self, account_number, pin):
        user = self.user_data.get(account_number)
        if user and user['pin'] == pin:
            self.current_user = account_number
            return True
        return False

    def get_balance(self):
        return self.user_data[self.current_user]['balance']

    def deposit(self, amount):
        self.user_data[self.current_user]['balance'] += amount

    def withdraw(self, amount):
        if self.user_data[self.current_user]['balance'] >= amount:
            self.user_data[self.current_user]['balance'] -= amount
            return True
        return False
