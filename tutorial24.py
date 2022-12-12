# append method

fruits = ["grapes", "apple"]
fruits.append("mango")
print(fruits)


# insert method

fruits1 = ["mango", "orange"]
fruits1.insert(2,"grapes")
print(fruits1)


# concatenate method

fruits1 = ["mango", "orange"]
fruits2 = ["grapes", "apple"]
fruits3 = fruits1 + fruits2
print(fruits3)


# extend method

fruits1 = ["mango", "orange"]
fruits2 = ["grapes", "apple"]
fruits1.extend(fruits2)
print(fruits1)
print(fruits2)