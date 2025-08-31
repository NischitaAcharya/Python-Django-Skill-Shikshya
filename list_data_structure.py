# animal_list = []
# ['cat','dog'] = ['cats','dogs']
#WAP to store combination of ["cat","dog","elephant","human"]
#create alist called animal_list and add names of animals in it. Append more annimals. manipulate (manipulate usign loop. <cat to cats dog to dogs> Use CRUD on LIST?


animal_list = ['cat', 'dog', 'lion','dog']

# Add(append) more animals

animal_list.append('tiger')
animal_list.append('elephant')
print(animal_list)

#insert(in specific place)

animal_list.insert(4,'cow')
print(animal_list)

# Remove animal from list

animal_list.remove('dog')  
print(animal_list)

#sort (according to alphabetical order)

animal_list.sort()
print(animal_list)

#pop (removes last item form list)

animal_list.pop()
print(animal_list)

#index ( find position of items)

print(animal_list.index('elephant'))

#reverse 

animal_list.reverse()
print(animal_list)

#count

print(animal_list.count('dog'))

#clear

animal_list.clear()
print(animal_list)









