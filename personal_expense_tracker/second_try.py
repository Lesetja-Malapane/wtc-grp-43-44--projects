import json
import os.path

def no_file(data):
    new = json.dumps(data, indent=2)
    with open('data.json', 'w') as new_file:
        new_file.write(new)
        

def open_file():
    with open('data.json', 'r') as file:
        data = json.load(file)

    return data

def category():

    category = {
        1: "Food",
        2: "Entertainment",
        3: "Transport",
        4: "Fees",
        5: "Other"
    }
     
    return category
    

def add_to_existing_list(data, category_list, username):

    expense = input("\nEnter your expense: ")
    description = input("\nEnter your description: ")


    for placement in category_list:
        print(f"{placement}: {category_list[placement]}")

    choose_category = int(input("Choose your category number: "))

    while choose_category not in category_list:
        choose_category = int(input("Please choose the correct category number: "))

    expense_category = category_list[choose_category]

    date = input("\nEnter date: ")

    new_data = {
        "Item_number": data[username][0]["Item_number"] + len(data[username]),
        "Expense": expense,
        "Description": description,
        "Category": expense_category,
        "Date": date
    }

    data[username].append(new_data)

    with open('data.json', 'w') as new_file:
        new = json.dumps(data, indent=2)
        new_file.write(new)

def add_to_non_existing_list(data, category_list, username):

    data.update({username: []})

    expense = input("\nEnter your expense: ")
    description = input("\nEnter your description: ")


    for placement in category_list:
        print(f"{placement}: {category_list[placement]}")

    choose_category = int(input("Choose your category number: "))

    while choose_category not in category_list:
        choose_category = int(input("Please choose the correct category number: "))

    expense_category = category_list[choose_category]

    date = input("\nEnter date: ")

    new_data = {
        "Item_number": 0,
        "Expense": expense,
        "Description": description,
        "Category": expense_category,
        "Date": date
    }

    data[username].append(new_data)

    with open('data.json', 'w') as new_file:
        new = json.dumps(data, indent=2)
        new_file.write(new)

def view_expenses(data, username):

    category = input("Enter Category: ")
    num = 0
    if username in data.keys():

        print("\nList of your Expenses: \n")
        for list in data[username]:
            if list["Category"].lower() == category.lower():
                num += 1
                print(f"{num}: {list}")
            else:
                continue
    else:
        print("\nUsername Not Found!!")


def main():

    template = {
    "username": [
        {
        "Item_number": 0,
        "Expense": "petrol",
        "Description": "fuel",
        "Category": "Transport",
        "Date": "27/07/2024"
        }]
    }

    if "data.json" not in  os.listdir():
        no_file(template)
    else:
        pass

    data = open_file()
    category_list = category()

    print("\nWelcome To Your Personal Expense Tracker\n")

    username = str(input("Enter Your Username: "))

    while True:

        print(f"***Welcome back!!! {username}***")

        if username in data.keys():


            answer = input("\nDo You Want To: \n1. Add a New Expense?: \n2. View Your Expense?: \n3. Exit?: \nYou selected option: ")

            while answer != "1" and answer != "2" and answer != "3":
                answer = input("\nEnter options given below \n1. Add a New Expense?: \n2. View Your Expense?:\n3. Exit?: \nYou selected option: ")

            else:
                if answer == "1":
                    add_to_existing_list(data, category_list, username)
                    print("\nExpense Added")
                    continue
                elif answer == "2":
                    print("\nChoose between options below: ")
                    for choice in category_list:
                        print(f"{category_list[choice]}")
                    view_expenses(data, username)
                    continue
                else:
                    print("\n***Thank You For using Our Services***")
                    return

        else:
            print("***Added New User***")
            answer = str(input("\nDo You Want To: \n1. Add a New Expense?: \n2. Exit?: \nYou selected option: "))

            while answer != "1" and answer != "2":
                answer = input("Enter options given below\n1. Add a New Expense?: \n2. Exit?: \nYou selected option: ")
                
            else:
                if answer == "1":
                    add_to_non_existing_list(data, category_list, username)
                elif answer == "2":
                    print("\n***Thank You For using Our Services***")
                    return

if __name__ == "__main__":
    main()