#dictionaries intro
#Q - why we use dictionaries?
#A =  Because of limitations of lists , lists are not enough to represent
# real date

# example
use = ["Harshit",24],["coco","kimi no na wa"],["awakening","fairy tale"]
# this list contains user name, age , fav movies, fav tunes
# you can do this but this is not a good way to do this

# Q - what are dictionaries
# A - unordered collectiobs of data in key : value pair.

# how to create dictionaries
user = {"name":"Harshit","age":24}
# print(user)
# print(type(user))


# second method to create dictionary
user1 = dict(name="Harshit", age = 24)
# print(user1)

# how to access data from dictionary
# NOTE - There is no indexing because of unordered collections of data.
print(user["name"])
print(use["age"])

# which type of data a dictionary can store?
# anything
# numbers,strings,listy ,dictionary,

user_info = {
    "name" : "harshit",
     "age" : 24,
     "fav movies" : ["cocoo","kimi no na wa"],
     "fav_tunes" :["awakening","fairy tale"],
}
# print(user_info["fav movies"])



# How ot add data to empty dictionary
user_info2 = {}
user_info2["name"] = "mohit"
user_info2["age"] = 19
print(user_info2)