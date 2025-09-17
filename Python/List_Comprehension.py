# List Comprehension

my_lists = [ 22,34,45,43,23,56]

#without list comp
square_list = []
for item in my_lists:
    square_list.append(item*item)
print("**Without List Comprehension",square_list)
    
    
#with using list comprehension
print("**Using List Comprehension")
square_list = [item*item for item in my_lists]
print(square_list)