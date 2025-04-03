marks = [94.1,87.5,95.4,45.25]

# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks)


# student = ["seiam", 95.4,"mymensingh"]
# student[0] = "mahmud"
# print(student)

# List Slicing
# list_name[starting_idx : ending_idx] ending idx is not included

# print(marks[1:4])
# print(marks[-3:-1])

# List Methods (Mutable)
# list = [2,1,3]
# list.append(4) #adds one element at the end [2,1,3,4] # return None
# list.sort() #shorts in ascending order [1,2,3]  # return None
# list.sort(reverse= True) #sorts in decending order [3,2,1]
# list.reverse() #reverses list [3,1,2]
# list.insert(idx, el) #insert element at index

# list.append(5)
# print(list) # [1, 2, 3, 4, 5]


# list.insert(1,100) # [1, 100, 2, 3, 4]
# print(list)
# list = [2,1,3,1]
# list.remove(1) #removes first occurrence of element # [2,3,1]
# # list.pop(idx) #removes elementnat idx

# print(list)





# Tuples in Python (Immutable)
tup = (2,1,5,1)
# tup1 = ()
# tup2 = (1,)
# print(type(tup))
# print(tup[2])
# print(tup[0:2])

# print(tup.index(5)) # return index
# print(tup.count(1)) # counts total occurrence

# Practice
# movies = []
# movie1 = input("Enter your first movie  ")
# movie2 = input("Enter your 2nd movie ")
# movie3 = input("Enter your 3rd movie ")


# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print(movies)



# list1 = [1,2,1]
list1 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palimdrome")
else:
    print("NOT a palimdrome")
