# pratice for loop
# ask user a number like 1
# calculate sum of digits ---> 1 + 2 + 5 + 6

# logic
# num="1256"
# int(num[0])---->1
# int(num[1])---->2
# int(num[2])---->5
# int(num[3])---->6
# i -----> 0 to 3

total=0
num=input("enter a number: ")
for i in range(0,len(num)):
    total += int(num[i])

print(total)