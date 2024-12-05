def dyne(n):
    return n * 10**5
    
def newton(n):
    return  n / 10**5

x = int(input("Enter the value:"))
convert = input("1. Newton to Dyne\n2. Dyne to Newton\n:")
match convert:
    case "1":
        result = dyne(x)
        print(f"{x} N = {result} D")

    case "2":
        result = newton(x)
        print(f"{x} D = {result} N")
