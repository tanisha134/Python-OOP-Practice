class Friend:
    #Constructor
    def __init__(self):
        self.Friends = ['soha','shafa','sharodia','yousra','asmita']#Instance attribute

    #For finding my friend's name 
    def find_frnd(self,friend_name):
        #condition
        if friend_name in self.Friends:
            return f"Your friend {friend_name} is in the list of Tanisha's Friendlist, so your friend has been founded <333"
        else:
            return f"This {friend_name} is not in the list , Sorry Tanisha!!!"
        
    #For adding a new friend 
    def adding_frnd(self,friend_name):
        if friend_name not in self.Friends:
            self.Friends.append(friend_name)
            print(f"Your Friend {friend_name} is added in your friend list Successfully")
        else:
            print(f"This friend is already in the friend list Tanisha , So You can not add her <3333")

    #For Removing a friend
    def remove_frnd(self,friend_name):
        if friend_name in self.Friends:
            self.Friends.remove(friend_name)
            print(f"Your {friend_name} is now deleted from your frnd list Tanisha")
        else:
            print(f"Your {friend_name} is not in the frnd list , so you can't remove her<333")

    #For Showing The frnd List
    def Show_frnds(self):
        if self.Friends:
          print("The Friend list are :"," _ ".join(self.Friends))

    #For Taking Input from user 
    def user_Choice(self):
        while True:
            self.Show_frnds()
            print("\n........== WeLcOmE tO mY Friend List ==........")
            print("1. => Search for a friend => ")
            print("2. => Be someone's friend => ")
            print("3. => Remove friend that you don't like => ")
            print("4. => exit => ")

            choice=input("Enter Any option among (1,2,3 and 4) : ").strip()
            if choice == "1":
                friend_name = input("Enter your friend name that you want to find Tanisha : ").strip().lower()
                print(self.find_frnd(friend_name))
            elif choice == "2":
                friend_name = input("Enter a New friend that you want to add Tanisha : ").strip().lower()
                self.adding_frnd(friend_name)
            elif choice == "3":
                friend_name = input("Enter a friend name that you want to remove Tanisha : ").strip().lower()
                self.remove_frnd(friend_name)
            elif choice == "4":
                print("Thanks for being my friends. That's all Bye <333")
                break
            else:
                print("Please Enter a valied option among 1,2,3 and 4 !!!")
# Creating an Object
beingFriends = Friend()
beingFriends.user_Choice() 





        
        
