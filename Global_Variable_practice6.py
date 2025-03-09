#global Varible
class Student:
    #Global varible 
    School ='Ankur Society Girls High School'

    @classmethod
    def change_school(cls,new_school):
        cls.School = new_school

#Calling the Change_method
Student.change_school("Nasirabad Girls High School")
print(Student.School)


