# practical for loop
# ask user name and count each character
# "Yunesh Kumar"
# Y: 1
# u: 2
# n: 1
# e: 1
# s: 1
# h: 1
#  : 1
# K: 1
# m: 1
# a: 1
# r: 1
name= input("enter your name : ")
temp =""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp +=name[i]