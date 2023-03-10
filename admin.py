import deta
import config
import os
import time

detaB = deta.Deta(config.api_key)
db = detaB.Base("command")


def edit_computer(data):
    pass


def delete_computer(key):   
    os.system("cls")
    print("#" * 20)
    print()
    choice = input(f"Are you sure you want to delete {key} (y/N)? ").lower()
    print()
    if choice == "y":
        print(f"Deleting '{key}'")
        time.sleep(0.5)
        db.delete(key)
    else:
        print("Cancelling Deletion")
        time.sleep(0.5)
    main()


def computer_management(data):
    accept = False
    while not accept:
        os.system("cls")
        print("#" * 20)
        print()
        print("Computer Management Menu")
        print()
        print(f"Selected Computer: {data['key']}")
        print("\n")
        print("1. Edit")
        print()
        print("2. Delete")
        print()
        print("3. Return to Main Menu")
        print("\n")
        accept = True
        choice = input("Choose an option: ")
        if not choice in ["1", "2", "3"]:
            accept = False
    if choice == "1":
        edit_computer(data)
    if choice == "2":
        delete_computer(data["key"])
    if choice == "3":
        main()

def main():
    res = db.fetch()
    comps = res.items
    accept = False
    while not accept:
        os.system("cls")
        print("#" * 20)
        print()
        print("List of Computers")
        print("\n")
        for compIdx in range(len(comps)):
            print(f"{compIdx+1}: {comps[compIdx]['key']}")
            print()
        print()
        accept = True
        choice = input("Choose a Computer Number: ")
        try:
            selectComp = comps[int(choice) - 1]
        except:
            accept = False
    computer_management(selectComp)

main()