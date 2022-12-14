# in keyword and iterations in dictionary 

user_info = {
    'name' :
    'harshit', 
    'age' : 24,
    'vav_movies': ['coco', 'kimi no wa'],
    'fav_tunes': ['awakening', 'fairy tale'],
}
# check if key exist in dictionary 
# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')

# check if value exist in dictionary ----> values methood 
# if 24 in user_info.values():
#     print('present')
# else:
#     print('not present')

# loops in dictionaries
# for i in user_info.values():
#     print(i)

# values method
# user_info_values=user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# user_info_keys = user_info.key()
# print(user_info_keys)
# print(type(user_info_keys))

# loop in dictionaries
# for i in user_info:
#     print(user_info[i])

# items method
# user_items= user_info.item()
# print(user_items)
# print(type(user_items))
# [('name', 'harshit'), ('age',24),('fav_movies',['coco', 'kimi no na wa'])]

for i,j in user_info.items():
    print(f"key is {i} and value is {j}")
