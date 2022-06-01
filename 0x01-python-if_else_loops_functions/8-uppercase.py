#!/usr/bin/python3
def uppercase(str):
       
# for each character in the string "str"    
for c in str:
    # check if the character is in lowercase
    if ord(c) >= 97 and ord(c) <= 122:
        # convert lowercase to upercase
        c = chr(ord(c) - 32)
        # print the formatted string
    print("{}".format(c), end="")
print("")
