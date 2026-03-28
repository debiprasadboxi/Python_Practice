## Dictionary in Python
## Dictionaries are used to store data values in key:value pairs.
## They are unordered, mutable(changeable) and don't allow duplicates keys.
## Syntex:
## dict = {key1:value1, key2:value2, key3:value3}

## Example1:
# info = {"key": "value", "name": "DebiBoxi", "learning": "Coding"}
# print(info)

## Example2:
## Even we can store list and tuple in dictionary
# info = {
#     "name": "DebiBoxi",
#     "learning": ["Python", "Java", "C++"],
#     "hobbies": ("Coding", "Gaming"),
# }
# print(info)

## Example3:
## Add new filed in dictionary and change the value of existing field
# info = {
#     "name": "DebiBoxi",
#     "age": 35,
#     "learning": ["Python", "Java"],
#     "hobbies": ("Coding", "Gaming"),
# }
# print(info)
# info["age"] = 36
# print(info)
# info["surname"] = "Boxi"
# print(info)

## Example4:
## Create a empty dictionary and add some key value pair in it
# info = {}
# print(info)
# info["name"] = "DebiBoxi"
# info["learning"] = ["python", "Java"]
# print(info)


## Example5:
## Nested Dictionary
# student = {
#     "name": "DebiBoxi",
#     "subject": {"math": 90.7, "science": 85.44, "english": 95.21},
# }
# print(student)
# print(student["subject"])
# print(student["subject"]["math"])


## Example6:
## Dictionary Methods1
## Keys() method returns a view object that displays a list of all the keys in the dictionary.
info = {
    "name": "DebiBoxi",
    "age": 35,
    "learning": ["Python", "Java"],
    "hobbies": ("Coding", "Gaming"),
    "subject": {"math": 90.7, "science": 85.44, "english": 95.21},
}
# print(info.keys())
# print(info["subject"].keys())
# print(list(info.keys()))
# print(list(info["subject"].keys()))
# print(len(info.keys()))


## Dictionary Methods2
## Values() method returns a view object that displays a list of all the values in the dictionary.
# print(info.values())
# print(info["subject"].values())

## we can convert the view object into list using list() method
# print(list(info.values()))
# print(list(info["subject"].values()))

## Dictionary Methods3
## items() method returns a view object that displays a list of dictionary's key-value as tuple pairs.
# print(info.items())
# print(info["subject"].items())
# print()
## we can convert the view object into list using list() method
# print(list(info.items()))
# print(list(info["subject"].items()))


## Dictionary Methods4
## get() method returns the value of the specified key. If the key does not exist,
## it returns None (or a default value if specified).
# print(info.get("name"))
# print(info["name"])
# print(info.get("non_existing_key"))  # This will return None
# print(info["non_existing_key"])  # Error

## Dictionary Methods5
## update() method updates the dictionary with the elements from another
# dictionary object or from an iterable of key/value pairs.

# print("Old Records:", info)
# new_dict = {"name": "Prasad Boxi", "age": 36, "gender": "Male"}
# info.update(new_dict)
# print("\nUpdated Records:", info)



