from tabulate import tabulate

# upper case for constant
HEADERS = ("Index", "Name", "Stock", "Price")

# function to display items
def show(table, headers=HEADERS, title="\nTabel Daftar Buah\n"):
    """function to display available items

    Args:
        table (list): Database
        headers (tuple, optional): Column names in the table. Defaults to HEADERS.
        title (str, optional): Table name. Defaults to "\nTabel Daftar Buah\n".
    """
    print(title)
    print(tabulate(table, headers, tablefmt="grid"))

# function to add an item
def add(table):
    """function to display a new item

    Args:
        table (list): Database
    """
    name = input("Input the fruit name: ")
    stock = input("Input number of the fruit you want to buy: ")
    price = input("Input the price: ")

    for i, item in enumerate(table):
        if name.capitalize() == item[1]:
            item[2] += int(stock)
            item[3] += int(price)
            break
        else:
            table.append([
                len(table) + 1,
                name,
                int(stock),
                int(price)
            ])

        show(table)

# function to remove an item
def delete(table):
    """function to remove an item

    Args:
        table (list): Database
    """
    while True:
        show(table)

        id = int(input("Input the index of the fruit: "))

        if id > len(table)-1:
            print("Index is out of reach!")
            continue

        for item in table:
            if id in item:
                table.remove(item)

        for idx, item in enumerate(table):
            if idx < item[0]:
                item[0] -= 1
        else:
            break

    show(table)

# function to purchase an item
def buy(table):
    CART = []
    reorder = "yes"
    while reorder != "no":
        show(table)
        while True:
            id = int(input("Input the fruit index: "))
            for item in table:
                if id in item:
                    id = id
                    break
            else:
                print("Fruit index is not found")
                continue
            break

    while True:
        quantity = int(input("Input the quantity of the fruit: "))
        for item in table:
            if id in item:
                if quantity > item[2]:
                    print("The number of stock is not enough")
                    break
                else:
                    CART.append([
                        item[1],
                        quantity,
                        item[3]
                    ])
                    break
        break

    show(CART, ["Name", "Qty", "Price"])

    confirm = input("Do you want to order again? [Yes/No]")
    if confirm == "no":
        reorder == "no"
    
    # Calculate total amount of purchase
    total = sum([item[-1] for item in CART])
    payment(total)

# function to pay the purchase
def payment(nominal):
    """function to make payment

    Args:
        nominal (int): Amount of money for payment
    """
    # request input
    while True:
        pay = input("Please input the amount of your money: ")
        # input validation
        if is_number(pay):
            # calculate the remainder
            if pay >= nominal:
                print(f"Your change is {pay - nominal}")
                break
            else:
                print(f"\nYou need to pay {nominal - pay}\n")
        else:
            print("Enter an amount!")

# function to validate numerical input
def is_number(value):
    try:
        int(value)
        return True
    except:
        return False