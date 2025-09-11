# # print num divisible by 3 and 5:

# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         print(i)
#     else:
#         continue

# # reverse the number:

# num = input("Enter your number: ")
# print(num[::-1])    

# # find the factorial in a function:

# def factorial(n):
#     x = n
#     fact = 1
#     i = 1
#     for i in range(n):
#         fact*=x
#         x-=1
#         i+=1
#     return fact

# n = int(input("Enter the number you want the factorial of: "))
# print(factorial(6))

# # find Armstrong number:

# num = input("Enter your number: ")
# new_num = list(map(int, (num)))
# var = 0
# for n in new_num:
#     var += n**3

# if str(var)== num:
#     print("Number is Armstrong")
# else:
#     print("Number is not Armstrong")

# # print factors of number:

# n = int(input("Enter your number: "))
# print("The factor is:")
# i = 1
# for i in range(i, n):
#     if n%i == 0:
#         print(i)