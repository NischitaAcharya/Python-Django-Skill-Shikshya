class person:
    def _int_(self,first_name):
        self.name = first_name
    
    def work(self):
        print(f"My name is {self.name} and I am working")
        
    def study(self):
        print(f"My name is {self.name} and I am studying")
        
Nis_instance = person("NisA")
Nis_instance.work()
Nis_instance.study()

Ram_object = person("Ram")
Ram_object.work()
Ram_object.study()

Shyam_instance = person("shyam")
Shyam_instance.study()
Shyam_instance.work()