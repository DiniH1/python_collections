# Python Data Collections

- lists
- tuples
- dicts
- sets


### Lists: (AKA array in other languages)
- Shopping list - multiple items
- add, edit, delete, update
- What is `CRUD` - `Create` `Read` `Update` `Delete`
# Let's create a shopping list
### Syntax [] - name of list = ["","",""]

`shopping_list = ["apples","eggs","dark chocolate","tea","bread"]`

`print(shopping_list) 
print(type(shopping_list))`

### How can access dark chocolate using the same conceptt rgat we learned yesterday INDEXING

`print(shopping_list[1]) #wll index the list and display eggs
print(shopping_list[-1]) # will index from the last position`

`shopping_list[0] = "mango"
 print(shopping_list)`


  ### append will an item to our shopping list
 shopping_list.append("tuna")
 print(shopping_list)
### .pop will delete an item of a list if the index is not specified it will delete the last item on the list
 `shopping_list.pop(3)`
`print(shopping_list)`

### We can have multiple data types in the same list
`mix_list = [1, 2, 3, "one", "two"]`

`essentials = ("paracetamol", "milk", "butter")`
`print(type(essentials))`
`essentials.pop(1)`
`print(essentials)`
## lists are mutable and tuples are immutable

# Dictionaries and sets are both data collections in python

## Dicts?

- dicts are another way to manage data but can be a little more dynamic
- Dict works as a JEY and VALUE
- KEY = the refernce of the object
- VALUE = What is the data storage mechanism you need to use
- Dynamic as it we have lists, and another dict inside a dict
- Syntax - name = {} as use {} brackets to declare a Dict
  -         Key =   Value
## Key
`students_1 = {"name": "James",
              "stream": "Devops",
              "Completed_lessons" : 4,
              "Completed_lessons_names": ["Data types", "Git and Github", "Operators", "Lidts and tuples"]}`


# Lets check if we have got the syntax right and print the dict
`print(students_1)
print(type(students_1))
print(students_1["stream"]) # This is how we can fetch the value saved in the key called "stream"
print(students_1["Completed_lessons_names"][1])
rint the second last index of the key completed_lessons_names:[]`

`print(students_1["Completed_lessons_names"][-2])`

## Could we apply CRUD on a Dict?
### Print the second last value in the dict

`students_1["Completed_lessons"] = 3
print(students_1["Completed_lessons"])`

`students_1["Completed_lessons_names"].remove("Operators")
print(students_1["Completed_lessons_names"])`

### We have some bulletin methods that we can use with dict
### To print all the keys keys()
`print(students_1.keys())`

## To print all the values
`print(students_1.values())`


### Sets are also Data collection
### Syntax name = {" ", " ", " "}
### What is the diff between sets and dict?
### Sets are unordered
`shopping_list = {"eggs", "tea", "milk"}
                #   0       1      2
print(shopping_list)
car_parts = {"engine", "wheels", "windows"}
print(car_parts)`
### Can we add anything to a set?
`car_parts.add("seats")`
### Can we reomve an item?
`car_parts.discard("wheels")
print(car_parts)`

