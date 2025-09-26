'''📖 Library Management System (Complete OOP Project)
Design a Python program to manage a Library Management System using Object-Oriented Programming concepts.'''

from abc import ABC , abstractmethod
class LibraryItem(ABC):
    count=0
    def __init__(self,title,price):
        self.title=title
        self.__price=price
        LibraryItem.increment()

    @abstractmethod
    def show_info(self):
        pass

    def get_price(self):
        return self.__price

    def __add__(self,other):
        return self.get_price()+other.get_price()
    def __lt__(self,other):
        return self.get_price()<other.get_price()
    def __gt__(self,other):
        return self.get_price()>other.get_price()
    def __eq__(self,other):
        return self.get_price()==other.get_price()
    
    @classmethod
    def increment(cls):
        cls.count+=1
    @classmethod
    def show_count(cls):
        print(f"Total library items: {cls.count}")
    
    @staticmethod
    def is_high_price(price):
        if price>500:
            return True
        else:
            return False
    
    def set_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Invalid price.")
    

class Book(LibraryItem):
    def __init__(self,title,price,author):
        super().__init__(title,price)
        self.author=author
    def show_info(self):
        print(f"Book {self.title} by {self.author} || Price: {self.get_price()}")
    

class SpecialEdition(Book):
    def __init__(self,title,price,author,edition):
        super().__init__(title,price,author)
        self.edition=edition
    def show_info(self):
        super().show_info()
        print(f"Book type: {self.edition}")
    
class Magazine(LibraryItem):
    def __init__(self,title,price,issue):
        super().__init__(title,price)
        self.issue=issue
    def show_info(self):
        print(f"Magazine {self.title} issued in {self.issue} || Price: {self.get_price()}")
    
class Member:
    mem_count=0
    def __init__(self,name,m_id):
        self.name=name
        self.m_id=m_id
        Member.inc_mem_count()
    def __str__(self):
        return f"Name: {self.name} || m_id: {self.m_id}"
    @classmethod
    def inc_mem_count(cls):
        cls.mem_count+=1
    @classmethod
    def show_mem_count(cls):
        print(f"Total members: {cls.mem_count}")

def main():
    items=[]
    members=[]

    while True:
        print("1.Add book\n2.Add Spl edition book\n3.Add magazine\n4.Add member\n5.Show all library items\n6.Show all members\n7.Show counts\n8.Exit")
        ch=input("Enter an option 1-8: ")
        if ch=='1':
            title= input("Enter title:")
            price= float(input("Enter price: "))
            author= input("Enter author of book: ")
            b= Book(title,price,author)
            items.append(b)
            print("Book appended successfully.")
        elif ch=='2':
            title= input("Enter title:")
            price= float(input("Enter price: "))
            author= input("Enter author of book: ")
            edition= input("Enter edition type: ")
            s= SpecialEdition(title,price,author,edition)
            items.append(s)
            print("Spl Edition Book appended successfully.")

        elif ch=='3':
            title = input("Enter magazine title: ")
            price = float(input("Enter price: "))
            issue = input("Enter issue date/month: ")
            m = Magazine(title, price, issue)
            items.append(m)
            print("Magazine added successfully.")

        elif ch=='4':
            name = input("Enter member name: ")
            m_id = input("Enter member ID: ")
            mem = Member(name, m_id)
            members.append(mem)
            print("Member registered successfully.")
        
        elif ch=='5':
            print("Library Items: ")
            if not items:
                print("No items yet.")
            else:
                for item in items:
                    item.show_info()
        
        elif ch=='6':
            print("Members: ")
            if not members:
                print("No members yet.")
            else:
                for mem in members:
                    print(mem)
        
        elif ch=='7':
            LibraryItem.show_count()
            Member.show_mem_count()
        
        elif ch=='8':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()
