# cheack if its even or odd:


num = int(input("Enter your number to check if its even or odd: "))

result=("EVEN" if num%2==0 else "ODD")
print(result)

# print the square:

num = int(input("Enter your number you want square of: "))
result = num**2
print(result)

# print number from 1 to 10 using for loop:

ran = int(input("Enter your range: "))
for i in range(1, ran+1):
    print(i)

# sum of two number:

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

print("The sum is", a+b)

# print the tabel of number:

num = int(input("Enter your number you want the tabel of: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
    i+=1