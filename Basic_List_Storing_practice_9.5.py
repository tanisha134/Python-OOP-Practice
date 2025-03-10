class Libray :
    # Global varible 
    Book = ['shafa', 'hafsa','tanisha']
    def __init__(self, book_name , pages):
        self.book_name = book_name #instace attribute
        self.pages = pages # instace attribute
    # intance method
    def display(self):
        print(f"Name : {self.book_name}\nPages : {self.pages}\nBook list : {Libray.Book}")


store = Libray('hira', 27)
store1 = Libray('hafsa', 50)
store.display()
store1.display()


