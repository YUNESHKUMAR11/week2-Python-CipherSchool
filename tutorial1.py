# sum from 1 to 10
# 1 + 2 + 3 ........ 10

# total=0 # + 1 + 2 +3 ......... 10
# for i in range(0,11):
#     total+=i

# print(total)
n=int(input("enter the number : "))
total=0
for i in range(1,n+1):
    total+=i
print(total)