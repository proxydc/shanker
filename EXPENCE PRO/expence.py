class Expense:
    def __init__(self, date, card, shop, amount, expense_type, shop_by):
        self.date = date
        self.card = card
        self.shop = shop
        self.amount = amount
        self.expense_type = expense_type
        self.shop_by = shop_by

def create_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    card = input("Enter card: ")
    shop = input("Enter shop: ")
    amount = float(input("Enter amount: "))
    expense_type = input("Enter type: ")
    shop_by = input("Enter shop by: ")
    return Expense(date, card, shop, amount, expense_type, shop_by)


expense = create_expense()
print("Expense created:")
print("Date:", expense.date)
print("Card:", expense.card)
print("Shop:", expense.shop)
print("Amount:", expense.amount)
print("Type:", expense.expense_type)
print("Shop by:", expense.shop_by)
