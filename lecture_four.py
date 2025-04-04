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



