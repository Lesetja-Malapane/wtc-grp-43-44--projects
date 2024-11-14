import json

def add_to_list():
        
    with open('data.json', 'r') as file:
        data = json.load(file)

    category = {
        1: "Food",
        2: "Entertainment",
        3: "Transport",
        4: "Fees",
        5: "Other"
    }

    name = input("Add to Who's List: ")

    if name in data.keys():
        expense = input("Enter your expense: ")
        description = input("Enter your description: ")


        for placement in category:
            print(f"{placement}: {category[placement]}")

        choose_category = int(input("Choose your category number: "))

        while choose_category not in category:
            choose_category = int(input("Please choose the correct category number: "))

        expense_category = category[choose_category]

        date = input("Enter date: ")

    # print(data)

        new_data = {
            "Item_number": data[name][0]["Item_number"] + len(data[name]),
            "Expense": expense,
            "Description": description,
            "Category": expense_category,
            "Date": date
        }

        data[name].append(new_data)

        with open('data.json', 'w') as new_file:
            new = json.dumps(data, indent=2)
            new_file.write(new)
    else:
        data.update({name: []})

        expense = input("Enter your expense: ")
        description = input("Enter your description: ")


        for placement in category:
            print(f"{placement}: {category[placement]}")

        choose_category = int(input("Choose your category number: "))

        while choose_category not in category:
            choose_category = int(input("Please choose the correct category number: "))

        expense_category = category[choose_category]

        date = input("Enter date: ")

    # print(data)

        new_data = {
            "Item_number": 0,
            "Expense": expense,
            "Description": description,
            "Category": expense_category,
            "Date": date
        }

        data[name].append(new_data)

        with open('data.json', 'w') as new_file:
            new = json.dumps(data, indent=2)
            new_file.write(new)


def view_expenses():


    with open('data.json', 'r') as file:
        data = json.load(file)

    view = input("View Expenses? Y/yes or N/no:")

    if view.lower() == 'y':
        name = input("Enter username: ")
        category = input("Enter Category: ")
        if name in data.keys():
            for list in data[name]:
                if list["Category"] == category:
                    print(list)
                else:
                    print("Category not Found!")
        else:
            print("Username Not Found!!")


def main():

    start = input("Do you want to add an item to your expense list?\nEnter Y/yes or N/no: ")

    if start.lower() == 'y' or start.lower() == 'yes':
        add_to_list()
    elif start.lower() == 'n' or start.lower() == 'no':
        view = input("Do you want to view your list?\nEnter Y/yes or N/no: ")
        if view == 'y':
            view_expenses()

    else:
        print("Thank You For Using Our Service")
            
main()
