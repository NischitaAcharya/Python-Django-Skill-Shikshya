# class person:
#     def _int_(self):
#         self.name = "Ram"
#         print("I am constructor Function...")
#         pass
    
# person_obj = person()
# print(person_obj.name)

#WAP to make a Employee Class where method are calculator_bonus,calculator_Total_salary.
#init methods takes as argument as name,total,salary,age,post and bonus_percentage.
#calculate_bonus function are used to calculate total bonus in flat, total_salary of bonus percentage
#and calculate_total_salary function are used to calculate totla salary received with including bonus given by company

# class Employee:
#     def _int_(self,name,total_salary,age,post,bonus_percentage):
#         #things to initialize
#         pass
    
#     def calculator_bonus(self):
#         #return total bonus received
#         return
    
#     def calculate_total_salary(self):
#         #return total salary with bonus
#         return
    
    
    
class Employee:
    def __init__(self, name, total_salary, age, post, bonus_percentage):
        self.name = name
        self.total_salary = total_salary
        self.age = age
        self.post = post
        self.bonus_percentage = bonus_percentage

    def calculator_bonus(self):
        bonus = (self.total_salary * self.bonus_percentage) / 100
        return bonus

    def calculate_total_salary(self):
        total_with_bonus = self.total_salary + self.calculator_bonus()     # Total salary including bonus
        return total_with_bonus


employee_1 = Employee("Nis", 50000, 30, "Manager", 10)

print(f"Employee Name: {employee_1.name}")
print(f"Bonus Received: {employee_1.calculator_bonus()}")
print(f"Total Salary with Bonus: {employee_1.calculate_total_salary()}")


