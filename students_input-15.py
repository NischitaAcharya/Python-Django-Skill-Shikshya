#WAP to take marks of "english" "computer","math" and studnet name from 5 students and display and make total( total marks from all the marks)
# {'Name':'A','English':21,'Computer':23,'Math':12}
# Step 1 : Create an empty list to store student data
# Step 2 : Loop to get data of 4 students
# Create dictionary for one student
 # Append student dictionary to the list
 # Display the list of students with their marks
 
#  for i in range(2):
#     print(f"\nEnter details for Student {i+1}:")
 
students = []

for i in range(1):
    student = {}
    
    student['Name'] = input("Enter Name: ")
    student['English'] = int(input("Enter English marks: "))
    student['Computer'] = int(input("Enter Computer marks: "))
    student['Math'] = int(input("Enter Math marks: "))
    
    student['Total'] = student['English'] + student['Computer'] + student['Math']
    
    students.append(student)

print("\nStudent Details:")
for s in students:
    print(s)
