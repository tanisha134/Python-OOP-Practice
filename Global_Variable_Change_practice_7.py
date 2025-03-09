class girl:
    # Global Variable
    School = 'BMS'
    #Constractor
    def __init__(self, name , age, home, roll ):
        # local Variable
        self.name=name
        self.age=age
        self.home=home
        self.roll=roll
        
    @classmethod
    def change_school(cls, new_school):
        cls.School=new_school
    
    # To show this function
    def show(self):
        print(f"Name is : {self.name} , Age is : {self.age} , Home is at : {self.home} , Roll is : {self.roll} Schol is : {self.School}")
        

# Changing the School 
girl.change_school("Aunkur Society Girls High School")

ba=girl('Sharodia', 13 , 'Muradpur',24)
ba.show()
ba1=girl('jakiya',14, 'shugondha',11)
ba1.show()
ba2=girl('Yousra', 13, 'Nasirabad',13)
ba2.show()
    
    
