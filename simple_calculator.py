def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def sub(*args):
    dif = args[0]
    for i in args:
        dif -= i
    return dif

def mul(*args):
    product = 1
    for i in args:
        product *= i
    return product

def div(*args):
    division = 1
    for i in args:
        division /= i
    return division

status = input("select: (add, sub, mul, div): ")
user_input = input("Enter numbers: ")
nums = [int(x) for x in user_input.split()]

if status == "add":
    print("sum:", add(*nums))
elif status == "sub":
    print("sub:", sub(*nums))
elif status == "mul":
    print("product:", mul(*nums))
elif status == "div":
    print("div:", div(*nums))
else:
    print("somthing went wrong!")