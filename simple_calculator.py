def add(x,y):
    z = x + y
    print(f"addition:{z}")
def subtraction(x, y):
    z = x - y
    print(f"subtraction:{z}")
def divide(x,y):
    z = x / y
    print(f"division:{z}")
def multiply(x,y):
    z = x*y
    print(f"multiplication:{z}")
X = int(input("enter the vlaue of x:"))
Y = int(input("enter the vlaue of y:"))
print("what kind of calculation do you want?")
choice = input("1. Addition \n2. Subtraction\n3. Division\n4. Multiplication \nEnter your choice:")

match choice:
    case "1":
        add(X,Y)
    case "2":
        subtraction(X,Y)
    case "3":
        divide(X,Y)
    case "4":
        multiply(X,Y)
