# generate lists with range functions 
# something more about pop method
# index method 
# pass list to a function 

# numbers = list(range(1,11))
# print(numbers)
# numbers=[1,2,3,4,5,6,7,8,9,10,1,5,6,7,8,1]
numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers.pop()
# print(numbers.pop())
# popped_item = numbers.pop()
# print(numbers)
# print(numbers.index(1, 11, 14))
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))


