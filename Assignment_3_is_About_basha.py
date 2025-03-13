class Bashar_Manush:
    def __init__(self):
        self.Family = ['hira mama','nanu','mili anty','ammu','naju anty','hafsa','mejho anty','boro mama','maimuna',' boro mami']#Instance Attribute

    #For finding Ghorer Shodosho
    def find_Family_Member(self,member_name):
        #Condition
        if member_name in self.Family:
            return f"Your Family member {member_name} is in the family list Tanisha,so you'r family member has been founded"
        else:
            return f"Sorry!!! Your Family  member {member_name} is not in the Family list"
    #For adding a new family member
    def adding_Family_member(self,member_name):
        if member_name not in self.Family:
            self.Family.append(member_name)
            print(f"Your family member {member_name} is added in your family list Successfully")
        else:
            print(f"Your this family member {member_name} is already in your family list Tanisha , so you can't add this family member <333333")
    #For removeing a family member 
    def Removing_Family_Member(self,member_name):
        if member_name in self.Family:
            self.Family.remove(member_name)
            print(f"Your This family member {member_name} is now deleted from your family list")
        else:
            print(f"Your Family member {member_name} is not in you Family list so,you can't remove this family member sorry!!!<333..")
    #For Showing the Family list
    def Show_Family(self):
        if self.Family:
            print("The Family list are :",' , '.join(self.Family))
    #For Taking From User Input
    def User_Choice(self):
        while True:
            self.Show_Family()
            print("\n........== WeLcOmE tO mY Family member List ==........")
            print("1. ==> Find a Family member ==> ")
            print("2. ==> Add a Family member ==> ")
            print("3. ==> Remove a Family member ==> ")
            print("4. ==> Exit ==> ")
            Choose =input("ENter Any Options Among 1,2,3 and 4 : ").strip()
            if Choose == "1":
             member_name = input("Enter your Family member name that you want to find Tannisha<3333 : ").strip().lower()
             print(self.find_Family_Member(member_name))
            elif Choose == "2":
                member_name = input("Enter Your Family member name that you want to add Tanisha : ").strip().lower()
                self.adding_Family_member(member_name)
            elif Choose == "3":
                member_name = input("Enter Your Family member name that you want to Remove Tanisha : ").strip().lower()
                self.Removing_Family_Member(member_name)
            elif Choose == "4":
                print(" That's all about my Family members byeee <333")
                break
            else:
                print("Please Enter a valied option among 1,2,3 and 4 !!!")

Family_Members = Bashar_Manush()
Family_Members.User_Choice()
