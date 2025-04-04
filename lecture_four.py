info = {
 "key":  "value",   
 "name":  "codeWithHarry",   
 "name":  "apnacollege",   # this took
 "subject": ["python", "c","javascript"],
 "topics": ("dict","set"),
 "learning":  "coding",   
 "age": 35,
 "is_adult": True,
 "marks": 94.4,
 50: 50,
 100.2: 253,
 ("hello","mahmud"): ("al mahmud",)
}
# print(info)
# print(info["subject"])
# print(info[50])
# print(type(info))
# info["age"] = 25
# print(info)

# info["surname"] = "Durjoy"
# print(info)



student = {
    "name": "Seiam al mahmud",
    "subjects":{
        "phy": 97,
        "chem": 90,
        "bio": 94,
        "math": 89,
    }
}
# print(student)
# print(student["subjects"])
# print(student["subjects"]["phy"])


# print(student.keys())
# print(list(student.keys()))
# print(type(list(student.keys()))) # <class 'list'>
# print(type(student.keys())) # <class 'dict_keys'>
# print(len(student.keys()))



# print(student.values())
# print(list(student.values()))


# print(student.items()) # dict_items([('name', 'Seiam al mahmud'), ('subjects', {'phy': 97, 'chem': 90, 'bio': 94, 'math': 89})])

# pairs = list(student.items())
# print(pairs[0])


# print(student["name2"]) # return error if it's not exist in dict
# print(student.get("name2")) # return no error although it's not exist in dict


# student.update({"city": "mymensingh"})
# print(student)








collection = {1,2,3,4,2,2, "world","world"} #unordered

# print(collection)
# print(len(collection))
# print(type(collection))

emtryCollection = set()
# print(emtryCollection) # set()
# print(type(emtryCollection))


newCollection = set()
newCollection.add(1)
newCollection.add(2)
newCollection.add(2)
newCollection.add(3)
# print(newCollection) # {1, 2}


# newCollection.remove(1)
# print(newCollection) # {2}


# newCollection.clear()
# print(newCollection.pop()) # random pick and remove
# print(newCollection.pop()) # random pick and remove
# print(newCollection) # set()



set1 = {1,2,3}
set2 = {2,3,4}
# set.union(set1)  # combines both set values & returns new
# set.intersection(set1)  # combines values & returns new


# print(set1.union(set2)) # {1, 2, 3, 4}
# print(set1.intersection(set2)) # {2, 3}


# Store following word meanings in a python dictionary: 
# table: "a piece of furniture", "list of facts & figures"
# "cat": "a small animal"

dictionary = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "list of facts & figures"]
}

# print(dictionary)


# You are given a list o subjescts for students. assume one classroom is required for  1 subject. How many classrooms are neded by all students.
    
#     "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C", 

subjects = {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C", 
}

# print(len(subjects)) # 5

# values = {9, 9.0, 9.25}
# print(values)
# values = {9, '9.0', 9.25}
# print(values)

values ={
    ("float", 9.0),
    ("int", 9),
}
print(values)