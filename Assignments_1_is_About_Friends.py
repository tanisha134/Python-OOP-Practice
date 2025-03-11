class Friend:
    #Constructor
    def __init__(self):
        self.Friends = ['soha','shafa','sharodia','yousra','asmita']#Instance attribute
    
    #for finding my friend
    def find_frnd(self,friend_name):
        #condition
        if friend_name in self.Friends:
            return f"Your friend {friend_name} is in the list Tanisha , so you'r friend has been founded<333"
        else:
            return f"This {friend_name} is not in the list , sorry Tanisha!!!"
    #For adding a new frnd
    def adding_frnd(self,friend_name):
        if friend_name not in self.Friends:
            self.Friends.append(friend_name)
            print(f"Your Friend {friend_name} is added in your frnd list Successfully")
        else:
            print(f"This frnd is already in the frnd list Tanisha , So You can not add her <3333")
    #For Removing a frnd
    def remove_frnd(self,friend_name):
        if friend_name in self.Friends:
            self.Friends.remove(friend_name)
            print(f"Your {friend_name} is now deleted from your frnd list Tanisha")
        else:
            print(f"Your {friend_name} is not in the frnd list , so you can't remove her<333")
    #For Showing The frnd List
    def Show_frnds(self):
        if self.Friends:
          print("The Friend list are :",' , '.join(self.Friends))

    #For Taking From User Input
    def user_Choice(self):
        while True:
            self.Show_frnds()
            print("\n........== WeLcOmE tO mY Friend List ==........")
            print("1. => find a friend => ")
            print("2. => be someone's friend => ")
            print("3. => remove friend that you don't like => ")
            print("4. => exit => ")
            choice=input("Enter Any option among (1,2,3 and 4) : ").strip()
            if choice == "1":
                friend_name = input("Enter your friend name that you want to find Tanisha : ").strip().lower()
                print(self.find_frnd(friend_name))
            elif choice == "2":
                friend_name = input("Enter a New friend that you want to add Tanisha : ").strip().lower()
                self.adding_frnd(friend_name)
            elif choice == "3":
                friend_name = input("Enter a friend name thet you want to remove Tanisha : ").strip().lower()
                self.remove_frnd(friend_name)
            elif choice == "4":
                print("Thanks for being my friends. That's all byeee <333")
                break
            else:
                print("Please Enter a valied option among 1,2,3 and 4 !!!")

beingFriends = Friend()
beingFriends.user_Choice() 





        
        
