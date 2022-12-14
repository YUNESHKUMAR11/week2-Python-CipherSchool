# fromkeys
# d = {"name":"unknown","age" : "unknown"}
d = dict.fromkeys(["name","age","height"],"unknown")
print(d)


# get method(useful)
d = {"name":"unknown","age" : "unknown"}
# print(d["names"])

print(d.get("name"))