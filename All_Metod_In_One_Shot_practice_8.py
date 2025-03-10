''''
1) Instance Method 
2) Class method
3) Static method 
4) Regular Method
'''

# Regular method 
def Greeting():
    print("Hello Everybody")

class student:
    #Gloval Attribute
    school = 'Ankur School'
    #Creating Constractor 
    def __init__(self, name , age, home):
        self.name =name #instace attribute
        self.age=age #instance Attribute
        self.home=home #instance Attribute
    
    #Intance Method (1 Number method)
    def Show(self):
        print(f"Name : {self.name} , Age : {self.age} , School : {self.school} , Location : {self.locaiton} , Home : {self.home}")
    
    #Class method (2 Number Method)
    @classmethod
    def change_school(cls, new_school, location):
        cls.school=new_school
        cls.locaiton = location

    #Static method   
    @staticmethod
    def add_numbers(a,b):
        return a+b

#Regular Method Calling 
Greeting()

# For Changing the Scool
student.change_school('Nasibar Girls School', '2 Number gate')

#Creating Object for Student Class
student1=student('Tanisha', 13,"Forida para")
student1.Show()
student2=student("Safa", 14,"Abashik")
student2.Show()

print("........This is Static method........")
#for static method
object=student.add_numbers(30, 40)
print("The Summation of two Numbers is : ",object)

