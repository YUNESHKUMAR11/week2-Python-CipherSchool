def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

# list, str
numbers=list(range(1,11))
number = square_list(numbers)