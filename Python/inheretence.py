class Person:
    def __init__(self):
        self.scientific_name = "Homo sapiens"
        
    def display(self):
        print("displaying...")
        
class Employee(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.__init__(self)
        
    def display_scientific_name(self):
        print(f"Scientific name of human is {self.scientific_name}")
        
    def get_total_bones():
        print("Total bonus is x")
        
emp_obj = Employee("Ram",25)
emp_obj.display()
# print(emp_obj.scientific_name)
emp_obj.display_scientific_name()



#WAP to make a parent class animal with methods sound and child class dog,cat,elephant,with methods food. Create childs class object and call sound, food.

class Animal:
    def sound(self):
        print("This animal makes a sound.")
        
class Dog(Animal):
    # def food(self):
    #     print("Dog eats bones.")
    def __init__(self,dog_sound,dog_food):
        Animal.__init__(self)

    def sound(self):
        print("Dog barks: Woof! Woof!")
        
class Cat(Animal):
    def food(self):
        print("Cat eats fish.")

    def sound(self):
        print("Cat meows: Meow! Meow!")
        
class Elephant(Animal):
    def food(self):
        print("Elephant eats grass and fruits.")

    def sound(self):
        print("Elephant trumpets: Pawoo!")
        
print("Dog:")
dog = Dog()
dog.sound()
dog.food()

print("\nCat:")
cat = Cat()
cat.sound()
cat.food()

print("\nElephant:")
elephant = Elephant()
elephant.sound()
elephant.food()