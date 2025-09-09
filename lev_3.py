# # even and odd list identification:

# even_list = []
# odd_list = []

# user_list = list(input("Enter your list: "))
# res = list(map(int, user_list))
# for s in res:
#     if s%2==0:
#         even_list.append(s)
#     else:
#         odd_list.append(s)
# print("your list =", res)
# print("Even list =", even_list)
# print("Odd list =", odd_list)


# # count the sentences words:

# sentence = input("Enter your sentence: ")
# list = sentence.split()
# for l in list:
#     print(f"The word {l.upper()} count is: {len(l)}")


# # calculate the sum of digits:

# user_digits = list((input("Enter your digit: ")))
# new_list = list(map(int, user_digits))
# print(f"The sum is: {sum(new_list)}")


# # frequency of string's each charactor:

# str = input("Enter your string: ")
# for s in str:
#     str_count = str.count(s)
#     print(f"The {s} count is: {str_count}")


#  simple calculator:

user_input = list((input("Enter your number: ")))
nums = list(map(int, user_input))
print(sum(nums))