option = """"
Please select any option
1. View Vegetable List
2. Add Vegetable
3. Delete Vegetable
4. Sort Vegetable List
5. Search Vegetable
6. Clear Vegetable List
7. Exit
"""

Vegetable_list = []

while True:
    print(option)
    user_input = input("Enter any Options (1-7):")
    
    if user_input == "1":
        print("\nVegetable List:", Vegetable_list)
        
    elif user_input == "2":
        item = input("Enter vegetable to add: ")
        Vegetable_list.append(item)
        print(f"'{item}' added to list.")
        
    elif user_input == "3":
        item = input("Enter vegetable to delete: ")
        if item in Vegetable_list:
            Vegetable_list.remove(item)
            print(f"'{item}' removed from list.")
        else:
            print(f"'{item}' not found in list.")
            
    elif user_input == "4":
        Vegetable_list.sort()
        print("Vegetable list sorted.")
        
    elif user_input == "5":
        item = input("Enter vegetable to search: ")
        if item in Vegetable_list:
            print(f"'{item}' is in the list.")
        else:
            print(f"'{item}' is not in the list.")
            
    elif user_input == "6":
        Vegetable_list.clear()
        print("Vegetable list cleared.")

            
    elif user_input == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid input. Please enter a number from 1 to 7.")