# listi = input("enter your list: ")
# positive_list = []
# new_list = list(map(int, listi.split()))
# for n in new_list:
#     if n>0:
#         positive_list.append(n)
# print(positive_list)

# uniqe_word = []
# for n in positive_list:
#     if n not in uniqe_word:
#         uniqe_word.append(n)

# print(uniqe_word)
while True:
    fruit = input("koi phal ka naam likhoo: \naby likh naa, \nin mai se choose kr\nApple\nanghoor\naam\nkela\nyahan likh: ")
    match fruit:
        case "Apple":
            print("nhi ye nhi likha tumne")
        case "anghoor":
            print("are langoor, anghoor nhi likha")
        case "aam":
            print("are bhai aam nhi he")
        case "kela":
            print("haan jii ye hui na baat ")
            break


