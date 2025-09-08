# # take the avg of 5 num:

# n1=int(input("Enter num 1: "))
# n2=int(input("Enter num 2: "))
# n3=int(input("Enter num 3: "))
# n4=int(input("Enter num 4: "))
# n5=int(input("Enter num 5: "))

# sum = n1 + n2 + n3 + n4 + n5
# print(sum/5)

# # max and min in list:

# list = [1,2,6,7,8,9]
# print(max(list))
# print(min(list))

# #  print reverse word

# word = input("Enter your word: ")
# reverse_word = word[::-1]

# print(reverse_word)

# # print if the number is prime or not

# n = int(input("Enter your number: "))
# is_prime = True

# for i in range(2, n):
#     if n%i==0:
#         is_prime = False
#         break
# if is_prime:
#     print("prime number")
# else:
#     print("not a prime")

# check if string is palindrom

str = input("Enter any string: ")
if str == str[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
