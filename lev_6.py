# Q1. Ek function multiply_list banao jo ek list ke numbers ko multiply karke result return kare.

# Q2. User se ek number input lo aur check karo ke prime hai ya nahi. (Prime check ke liye loop use karo)

# Q3. Ek list mein 1 se 20 tak numbers store karo. Sirf even numbers print karo.

# Q4. Ek dictionary student banao jisme name, age aur grade store ho aur phir uske values print karo.

# Q5. Ek function likho reverse_string(text) jo koi bhi string le aur reverse karke return kare.


def multiply_list():
    multiply = 1
    for l in my_list:
        multiply = multiply*l
    return multiply
list_as_str = input("Enter your list: ")
list_as_list = list_as_str.split()
my_list = list(map(int, list_as_list ))   
    
print(multiply_list())

# n = int(input("Enter your number: "))
# is_prime = True
# for i in range(2,n):
#     if n%i == 0:
#         is_prime = False
#         break

# if is_prime == True:
#     print("prime")
# else:
#     print("not prime") 

# even_list = []
# i = 1
# for i in range(1,21):
#     if i%2==0:
#         even_list.append(i)
# print(even_list)

# student = {
#     "name" : "sohana",
#     "age" : 17,
#     "grade" : "A+"
# }

# print(student.values())

# def reverse_str(n):
#     return n[::-1]

# n = input("Enter your string: ")
# print(reverse_str(n))