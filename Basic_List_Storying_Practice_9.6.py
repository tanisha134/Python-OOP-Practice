class Libray : 
    def __init__(self):
        self.book =['soha', 'jakiya','hafsa','tanisha']
    
    def order_book(self,Book_name):
        if Book_name in self.book:
            print(f"this {Book_name} is availbale in the Library sir <3 ")
        else:
            print("this Book is not Available in the Library Sorry sir ")


store = Libray()
Book_name =input("Enter any Books that want to order : ").strip().lower()
store.order_book(Book_name)


