expenses = []

#--Helper functions-- 

def get_valid(a):
    while True:
        try:
            amt = int(input(f'Enter expense {a}:')) 
            print('✅')
            return amt
            break
        except ValueError: print(f'❌Please enter {a} in digits')
        
#---------- core functions -add-view-delete-statistics-filter -------

def add_expense():
    name = input('Enter expense name:')
    amount = get_valid('amount')
    category = input('Enter category name:')
    date = input('Enter date(optional):')

    expense =     {
        'Name':name,
        'Amount':amount,
        'Category':category,
        'Date': date
    }
    expenses.append(expense)

    print(f'Expense named {name} of Rs{amount} added✅!!')

def view_expense():
    print('-- Expenses --')
    for i in expenses:
        print(f'{(expenses.index(i))+1}. {i.get('Name')} - {i.get('Amount')} | {i.get('Category')} | {i.get('Date')}')

def delete_expense():
    view_expense()
    expense_index = (get_valid('no')-1)
    inlist = False
    for i in expenses:
        if expense_index == expenses.index(i):
            print(f'Expense named {expenses[expense_index].get('Name')} of Rs{expenses[expense_index].get('Amount')} deleted✅!!')
            expenses.pop(expense_index)
            inlist= True
    if inlist == False:
         print('⁉️Expenses not found!!')

def show_statitics():
    total = 0
    for i in expenses:
       total += i.get('Amount')
    
    highest = 0
    lowest = expenses[0].get('Amount')
    for i in expenses:
        amt = i.get('Amount')

        if (amt)>highest:
             highest = amt

        if (amt)<lowest:
             lowest = amt 
    print(f'Total expenses🔻:Rs {round(total)}')
    print(f'Avarage expenses📊:Rs {round(total/len(expenses))}')
    print(f'Highest expense⬆️:Rs {round(highest)}')
    print(f'Highest expense⬇️:Rs {round(lowest)}')

def filter_category():
    category = input('Enter category to filter:')
    inlist = False
    
    for i in expenses:
           if i.get('Category') in category:
                print(f'{(expenses.index(i))+1}. {i.get('Name')} - {i.get('Amount')} | {i.get('Category')} | {i.get('Date')}')
                inlist= True

    if inlist == False:
        print('⁉️Category not in list yet!')

def main_menu():
    print("""
--- Expense Tracker ---
1. Add Expense
2. View All Expenses
3. Delete Expense
4. Show Statistics
5. Filter by Category
6. Exit
""")
    while True:
     try:
         choice = int(input('Enter your choice(1-6):'))
         return choice
     except ValueError: print('⁉️Please enter a valid option!')
   
while True:

    choice = main_menu()
    if choice == 1:
        print()
        add_expense()
    elif choice == 2:
        print()
        view_expense()
    elif choice == 3:
        print()
        delete_expense()
    elif choice == 4:
        print()
        show_statitics()
    elif choice == 5:
        print()
        filter_category()
    elif choice == 6:
        print()
        print('Thank you!🙏')
        break
    else: 
        print()
        print('Please enter between(1-6)!')
