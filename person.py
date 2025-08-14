class person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age

    def greet(self):
        if self.age >=18:
            print(f" {self.name} your are {self.age} years old")
        else:
            print(f"{self.name} you are young ")
        
       
         
        


# creating an object or instance of a person
individual1 = person("Queen",30)
individual2 = person("Peace",19)
individual3 = person("Exause",10)
individual4 = person("Rose",15)

#calling the greet method on the object
individual1.greet()
individual2.greet()
individual3.greet()
individual4.greet()

  
    


