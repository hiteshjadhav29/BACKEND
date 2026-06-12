x=[[1,"car",500],[2,"doll",1000],[3,"grocery",2000],[4,"sunglasses",5000]]
choice=0
while choice!=6:
    print("1.view product\n 2.add product\n 3.update product\n 4.buy product\n 5.delete product\n 6.search product\n")
    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            for i in x:
                print(x)
        case 2:
            n = int(input("enter number of products to add "))

            for i in range(n):
                print(f"\nEnter Details of Product {i+1}")
                ids=int(input("enter product id: "))
                pro=input("enter product name: ")
                pri=int(input("enter product price: "))
                x.append([ids,pro,pri])
            print(f"{n} products added succesfully")
        case 3:
            pid=int(input("enter product id: "))
            print("1.update name\n 2.update price\n 3.update both")
            ch=int(input("enter your choice: "))
            if ch==1:
                val=input("enter new product name")
                x[pid-1][ch]=val
                print(x)
            elif ch==2:
                val=int(input("enter new price"))
                x[pid-1][ch]=val
                print(x)
            elif ch==3:
                n=input("enter new name")
                p=int(input("enter new price"))
                x[pid-1][1]=n
                x[pid-1][2]=p
                print(x)
            else:
                print("invalid choice")
                
        case 4:
            total = sum(p[2] for p in x)
            gst = total * 0.05
            final_amount = total + gst

            print(f"Total Price : {total}")
            print(f"GST (5%)    : {gst}")
            print(f"Final Amount: {final_amount}")

        
        case 5:
            print("\n1. Delete One Product")
            print("2. Delete All Products")

            opt = int(input("Enter option: "))

            match opt:
                case 1:
                    pid = int(input("Enter Product ID to Delete: "))

                    for p in x:
                        if p[0] == pid:
                            x.remove(p)
                            print("Product Deleted Successfully.")
                            break
                    else:
                        print("Product ID Not Found.")

                case 2:
                    x.clear()
                    print("All Products Deleted Successfully.")

                case _:
                    print("Invalid Option")

        
        case 6:
            print("\n1. Search by ID")
            print("2. Search by Name")

            opt = int(input("Enter option: "))

            match opt:
                case 1:
                    pid = int(input("Enter Product ID: "))

                    for p in x:
                        if p[0] == pid:
                            print("Product Found:", p)
                            break
                    else:
                        print("Product Not Found.")

                case 2:
                    pname = input("Enter Product Name: ").lower()

                    for p in x:
                        if p[1].lower() == pname:
                            print("Product Found:", p)
                            break
                    else:
                        print("Product Not Found.")

                case _:
                    print("Invalid Option")
                
        case _:
            print("invalid choice")
