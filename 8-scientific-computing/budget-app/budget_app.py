class Category:
    def __init__(self, name) -> None:
        self.name = name
        self.balance = 0
        self.ledger = []
    
    def __str__(self):
        r = self.name.center(30, '*') + '\n'
        for entry in self.ledger:
            r += entry["description"].ljust(23)[:23] + f'{entry["amount"]:.2f}'.rjust(7)[-7:] + '\n'
        r += f'Total: {self.balance:.2f}'
        return r

    def deposit(self, amount, description = ""):
        self.balance += amount 
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -1 * amount, "description": description})            
            return True
        else:
            return False
   
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, dest):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {dest.name}')
            dest.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

  
    def check_funds(self, amount):
        return self.balance >= amount

    
def create_spend_chart(categories):
    balances = [cat.balance for cat in categories] 
    pers = [round(bal * 10 / sum(balances)) for bal in balances]
    
    r = "Percentage spent by category"

    for i in range(10, -1, -1):
        r += '\n' + str(i * 10).rjust(3) + '| ' 
        
        for per in pers:
            r += 'o  ' if per >= i else '   '
            
    r += "\n    ----------"

    names = [cat.name for cat in categories] 
    max_length = max(len(s) for s in names)

    for i in range(max_length):
        r += '\n' + ' ' * 5
        for word in names:
            r += word[i] + '  ' if i < len(word) else '   '

    return r
