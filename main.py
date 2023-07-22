from inventory import bookslist
def update():
    with open("inventory.py","w") as f:
        f.write("bookslist = ")
        f.write(str(bookslist))
while True:
    print("********************BOOK SHOP********************\n")
    print("1. See Inventory")
    print("2. Add book to Inventory")
    print("3. Buy a Book")
    print("4. Exit")
    task = int(input("Select a task:"))
    print()
    if task==1:
        print("****************INVENTORY****************")
        for i,n in enumerate(bookslist):
            print(i+1,")",n[0],"\nby",n[1],"\nPrice:",n[2],"\nQuantity:",n[3],"\n")    
    elif task==2:
        name = input("Enter the book name:").upper()
        author = input("Enter the author's name:").upper()
        price = int(input("Enter the price:"))
        quan = int(input("Quantity:"))
        t=0
        for i in bookslist:
            if (name==i[0]) and (author==i[1]):
                nquan = i[3]+quan
                i.pop()
                i.pop()
                i.append(price)
                i.append(nquan)
                t=1
                print("Book already in store :)")
                print("Quantity Updated!\n")
                
        if t==0:
            book = [name,author,price,quan]
            bookslist.append(book)
            print("Book added to store :)\n")
        update()
        
        
    elif task==3:
        bname = input("Search for a book:").upper()
        bauthor = input("Enter author's name:").upper()
        print()
        sig = 1
        for i in bookslist:
            if (bname==i[0]) and (bauthor==i[1]):
                print("Found a Book:")
                print("Book Name:",i[0])
                print("Author Name:",i[1])
                print("Price:",i[2])
                print("Quantity:",i[3])
                sig = 0
                while True:
                    confirm = input("Want to buy? (yes or no):").upper()
                    if (confirm=="YES") or (confirm=="Y"):
                        amount = int(input("How many books do you want to buy:"))
                        if amount>i[3]:
                            print("Sorry, We don't have that much of Books!")
                            break
                        else:
                            newquan = i[3]-amount
                            i.pop()
                            i.append(newquan)
                            print("Book Purchased Successfully!!\n")
                            break
                    elif (confirm=="NO") or (confirm=="N"):
                        print("Purchase Cancelled :(\n")
                        break
                    else:
                        True
        if sig==1:
            for i in bookslist:
                if (bname==i[0]) or (bauthor==i[1]):
                    print("Cannot find the exact book but here are some books which i guess you've been looking for :D\n")
                    print("Book Name:",i[0])
                    print("Author Name:",i[1])
                    print("Price:",i[2])
                    print("Quantity:",i[3])
                    confirm = input("Is this the book? (yes or no):").upper()
                    if (confirm=="YES") or (confirm=="Y"):
                        amount = int(input("How many books do you want to buy:"))
                        if amount>i[3]:
                            print("Sorry, We don't have that much of Books!")
                            break
                        else:
                            newquan = i[3]-amount
                            i.pop()
                            i.append(newquan)
                            print("Book Purchased Successfully!!\n")
                            break
                    elif (confirm=="NO") or (confirm=="N"):
                        continue
        update()
    elif task==4:
        print("Program Terminated...")
        break
    else:
        print("Please type 1,2,3 or 4 to perform your task!\n")