age=int(input("enter age"))
def isEli(age):
    try:
        if age>18:
            print("eligible")
        else:
            print("not eligible")
    except Exception as e:
        print(e)
isEli(age)        
