import market

database = [
    [0, "Apel", 20, 10_000],
    [1, "Jeruk", 15, 15_000],
    [2, "Anggur", 25, 20_000],
    [3, "Nanas", 10, 25_000]
]

headers = ["Index", "Name", "Stock", "Price"]

main_menu = f"""
List Menu:
1. Show
2. Add
3. Delete
4. Buy
5. Exit

Which number do you want to choose?
"""

def main():
    while True:
        choice = input(main_menu)
        if choice == "1":
            market.show(database)
        elif choice == "2":
            market.add(database)
        elif choice == "3":
            market.delete(database)
        elif choice == "4":
            market.buy(database)
        elif choice == "5":
            break
        else:
            print("Input number 1-5")
            continue

main()