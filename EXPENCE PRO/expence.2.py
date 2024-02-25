class Expense:
    def __init__(self, date, card, shop, amount, expense_type, shop_by):
        self.date = date
        self.card = card
        self.shop = shop
        self.amount = amount
        self.expense_type = expense_type
        self.shop_by = shop_by

cards = ["hello", "burse"]
shops = ["lidl", "leclerc", "tamil kadai"]
persons = ["amma", "srgs", "sachindra"]

def initialize_expense():
    date = input("Enter date (YYYY-MM-DD): ")

    print("Select a card:")
    for i, card in enumerate(cards):
        print(f"{i + 1}. {card}")
    card_index = int(input("Enter card number: ")) - 1
    card = cards[card_index]

    print("Select a shop:")
    for i, shop in enumerate(shops):
        print(f"{i + 1}. {shop}")
    shop_index = int(input("Enter shop number: ")) - 1
    shop = shops[shop_index]

    amount = float(input("Enter amount: "))

    print("Select expense type:")
    print("1. Food Item")
    print("2. House Item")
    expense_type_choice = int(input("Enter expense type number: "))
    expense_type = "Food Item" if expense_type_choice == 1 else "House Item"

    print("Select a person:")
    for i, person in enumerate(persons):
        print(f"{i + 1}. {person}")
    person_index = int(input("Enter person number: ")) - 1
    shop_by = persons[person_index]

    return Expense(date, card, shop, amount, expense_type, shop_by)

def add_to_list():
    expense_list = []
    while True:
        expense = initialize_expense()
        expense_list.append(expense)
        print("Expense added to the list.")
        end = input("Press 'q' to end or any other key to add another expense: ")
        if end.lower() == 'q':
            break
    return expense_list

def initialize_table(expense_list):
    table_content = []
    table_content.append("{:<12} {:<15} {:<20} {:<12} {:<10} {:<15}".format("Date", "Card", "Shop", "Amount", "Type", "Shop By"))
    table_content.append("-" * 90)
    for expense in expense_list:
        table_content.append("{:<12} {:<15} {:<20} {:<12.2f} {:<10} {:<15}".format(expense.date, expense.card, expense.shop, expense.amount, expense.expense_type, expense.shop_by))
    return table_content

def write_to_file(content):
    with open("srgs.txt", "w") as file:
        for line in content:
            file.write(line + "\n")


expense_list = add_to_list()
table_content = initialize_table(expense_list)
write_to_file(table_content)

