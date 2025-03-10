class Library:
    #Global Varible 
    Book=['funny story', 'sad story', 'ghost story' , 'adventure story']
    #Constractor
    def __init__(self, Book_name, pages):
        self.Book_name=Book_name # instance attribute
        self.pages=pages # instance Attribute

        #conditiaon 
        if self.Book_name in Library.Book:
            print(f"{self.Book_name} is availbale in the Book list sir <3")
        else:
            print(f"{self.Book_name} is not Available in the book List sir sorry for that!!!")

    #instanee method 
    def show(self):
        print(f"Book name : {self.book_name}, Number of Pages : {self.pages}")
        

print("..................WELCOME TO MY LIBRARY SIR.....................")
print("Witch book are you looking for sir???")
object1=Library('funny story', 100)
object2=Library('sad story',25)
object3=Library('ghost story', 100)
object4=Library('adventure story', 50)
object5=Library('love story', 50)