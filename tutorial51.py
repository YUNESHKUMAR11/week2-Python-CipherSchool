# looping in tuples 
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple 
# some functions that you can use with tuples 

mixed = (1,2,3,4.0)

# for loop and tuple 
# for i in mixed :
#     print(i)
# NOTE- You can use while loop too 

# tuple with one element 
nums=(1,)
words= ('word1')
# print(type(nums))
# print(type(words))

# tuple without parenthesis 
guitars = 'yamaha','baton rouge','taylor'
# print(type(guitars))

# tuple unpacking
guiterists=('Maneli Jamal','Eddie Van Der Meer','Andrew Foy')
guiterist1,guiterist2,guiterist3=(guiterists)
# print(guiterist1)

# list inside tuples
favorites = ('southern magnolia', ['Tokyo Ghoul Thene', 'landscape'])
# favorites[1].pop()
favorites[1].append("we made it ")
print(favorites)

# min(),max()
# print(min(mixed)) 
print(max(mixed))