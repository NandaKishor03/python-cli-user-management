class Node:
    def __init__(self,data):
        self.page = data
        self.next = None
        self.prev = None


class History:
    def __init__(self):
        self.head = Node("HomaPage")
        self.Current = self.head

    def search(self,name):
        newPage = Node(name)
        self.Current.next = newPage
        newPage.prev = self.Current
        self.Current = newPage

    def display(self):
        temp = self.head
        print("\n  ----------   Browsering History   -----------\n")
        while temp:
            print(temp.page,end = " -> " if temp.next else "\n")
            temp = temp.next

    def goPrev(self):
        if self.Current.prev:
            self.Current = self.Current.prev
            print("\n   ------------    You are in ",self.Current.page,"    --------------")
        else:
            print("\n  -------   ERROR   -------       It's the Default Page")

    def goNext(self):
        if self.Current.next:
            self.Current = self.Current.next
            print("\n   ------------    You are in ",self.Current.page,"    --------------")
        else:
            print("\n  -------   ERROR   -------       It's the Last Page")


def main():
    h = History()
    print("\n")
    print("    ---------------     Your are in HomePage    -----------------")
    while True:
        print("\n")
        print("Enter 1 to Search the Website")
        print("Enter 2 to go to the Previous Website")
        print("Enter 3 to go to the Next Website")
        print("Enter 4 to View your Path")
        print("Enter 5 to Exit for Browser")

        print("\n")
        option = int(input("Enter your Choice : "))
        
        if option == 1:
            print("\n")
            website = input("Enter Website name : ")
            h.search(website)
        elif option == 2:
            h.goPrev()
        elif option == 3:
            h.goNext()
        elif option == 4:
            print("\n")
            h.display()
        elif option == 5:
            break
        else:
            print("Please Enter correct option")
    
    print("\n")
    print("    ****************    Successfully Exited from the Browser    ****************\n")
    return

main()