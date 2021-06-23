# Dictionaries and sets are both data collections in python

## Dicts?
### sets?

# dicts are another way to manage data but can be a little more dynamic
# Dict works as a JEY and VALUE
# KEY = the refernce of the object
# VALUE = What is the data storage mechanism you need to use
# Dynamic as it we have lists, and another dict inside a dict
# Syntax - name = {} as use {} brackets to declare a Dict
#           Key =   Value
# Key
students_1 = {"name": "James",
              "stream": "Devops",
              "Completed_lessons" : 4,
              "Completed_lessons_names": ["Data types", "Git and Github", "Operators", "Lidts and tuples"]}


# Lets check if we have got the syntax right and print the dict
# print(students_1)
# print(type(students_1))
# print(students_1["stream"]) # This is how we can fetch the value saved in the key called "stream"
# print(students_1["Completed_lessons_names"][1])
# # print the second last index of the key completed_lessons_names:[]
#
# print(students_1["Completed_lessons_names"][-2])
#
# # Could we apply CRUD on a Dict?
# # Print the second last value in the dict
#
# students_1["Completed_lessons"] = 3
# print(students_1["Completed_lessons"])
#
# students_1["Completed_lessons_names"].remove("Operators")
# print(students_1["Completed_lessons_names"])

# We have some bulletin methods that we can use with dict
# To print all the keys keys()
# print(students_1.keys())

# To print all the values
# print(students_1.values())


# Sets are also Data collection
# Syntax name = {" ", " ", " "}
# What is the diff between sets and dict?
# Sets are unordered
shopping_list = {"eggs", "tea", "milk"}
                #   0       1      2
print(shopping_list)
car_parts = {"engine", "wheels", "windows"}
print(car_parts)
 # Can we add anything to a set?
car_parts.add("seats")
 # Can we reomve an item?
car_parts.discard("wheels")

print(car_parts)

