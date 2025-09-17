#WAP to crud on list
#WAP to give option to select choices as (display,append,deleat) from list.
#[]-- user_input
#options:
#display list, append item on list, delete item from list

option = """"
Please select any option
1. display items
2. append item on list
3. remove item from list
"""

user_list = []
while True:
    print(option)
    user_input = input("Enter any Options :")
    
    if user_input == "1":
        print(user_list)
        
    elif user_input == "2":
        item = input("Enter item to append: ")
        user_list.append(item)
        print(f"'{item}' appended to list.")
        
    elif user_input == '3':
        item = input("Enter item to delete: ")
        if item in user_list:
            user_list.remove(item)
            print(f"'{item}' removed from list.")
        else:
            print(f"'{item}' not found in list.")
            
        
        