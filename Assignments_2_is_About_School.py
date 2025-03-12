class School:
    def __init__(self):
        self.schools = ['bms','nasirabad girs school','aunkur school']#Instance attribute

    #For choosing a school
    def choose_school(self,school_name):
        #Condition
        if school_name in self.schools:
            return f"Tanisha Your This scl {school_name} is allready in the School list , You'r school has been chossed<333333"
        else:
            return f"Tanisha Your This Scl {school_name} is not in the list , sorry for that!!!"
    #For adding a new scl
    def adding_scl(self,school_name):
        if school_name not in self.schools:
            self.schools.append(school_name)
            print(f"Your scl {school_name} is added in your scl list Successfully")
        else:
            print(f"Your scl is already in your scl list Tanisha , so you can't add this scl Sorry<33")
    #For removing a scl
    def Removing_scl(self,school_name):
        if school_name in self.schools:
            self.schools.remove(school_name)
            print(f"Your scl {school_name} is now deleted from your scl list Tanisha")
        else:
            print(f"Your scl {school_name} is not in the scl list , so you can't remove this scl <333")
     #For Showing The scl List
    def display_scl(self):
           if self.schools:
               print("The School list are :",' , '.join(self.schools))

     #For Taking From User Input
    def User_Choice(self):
        while True:
            self.display_scl()
            print("\n.......... Welcome To My School List Everyone .......... ")
            print("1. => find a scl that you want => ")
            print("2. => Add a new scl to the list => ")
            print("3. => remove a scl that you don't want => ")
            print("4. => exit => ")
            choice=input("Enter Any option among (1,2,3 and 4) : ").strip()
            if choice == "1":
                school_name = input("Enter a school name that you want to choose Tanisha : ").strip().lower()
                print(self.choose_school(school_name))
            elif choice == "2":
                school_name = input("Enter a school name that you want to add Tanisha : ").strip().lower()
                self.adding_scl(school_name)
            elif choice == "3":
                school_name = input("Enter a school name that you want to remove Tanisha : ").strip().lower()
                self.Removing_scl(school_name)
            elif choice == "4":
                print("That's all byeee <333")
                break
            else:
                print("Please Enter a valied option among 1,2,3 and 4 !!!")

hmm = School()
hmm.User_Choice()


           