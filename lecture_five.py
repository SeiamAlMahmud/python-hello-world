# count = 1
# while count <= 500 :
#     print("hello world")
#     count += 1

# print(count)



#print numbers from 1 to 5
# i = 5
# while i >= 1 :
#     print(i)
#     i -= 1

# print(i)

# Print numbers from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i +=1


# Print numbers from 100 to 1.
# i = 100
# while i >= 1:
#     print(i)
#     i -=1


# Print the multiplicaiton table of a number n.
# n = 3
# count = 1
# while count <= 10:
#     print(count * n)
#     count +=1


# Print the elements of the following list using a loop:
# numbs = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(numbs):
#     print(numbs[idx])
#     idx +=1


# Search for a number x in this tuple using loop

# numbs = (1,4,9,16,25,36,49,64,25,81,100)
# x = 25
# idx = 0
# while idx < len(numbs):
#     if numbs[idx] == x:
#         print("Found at index", idx)
#     else:
#         print("Finding...")
#     idx +=1




# Break & continue
# Break: used to terminate the loop when encountered.
# Continue: terminates execution in the current iteration & continues execution of the loop



# x = 25
# idx = 0
# while idx < len(numbs):
#     if numbs[idx] == x:
#         print("Found at index", idx)
#         break
#     else:
#         print("Finding...")
#     idx +=1


# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue # skip # number 3 never print
#     print(i)
#     i += 1

# print only odd numbers 
# i = 1
# while i <= 20:
#     if(i % 2 == 0):
#         i += 1
#         continue # skip # number 3 never print
#     print(i)
#     i += 1


    
# print only even numbers 
# i = 1
# while i <= 20:
#     if(i % 2 != 0):
#         i += 1
#         continue # skip # number 3 never print
#     print(i)
#     i += 1














# Loops in Python


# numbs = (1,4,9,16,25,36,49,64,25,81,100)
# for val in numbs:
#     print(val)

# str = "apna college"
# for char in str:
#     print(char)
# else: # work when loop enda
#     print("END")






# using for 
# Print the elements of the following list using a loop:
# numbs =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100,49]
# for val in numbs:
#     print(val)



# x = 49
# idx = 0
# for el in numbs:
#     if(el == x):
#         print("number found at idx ",idx)
#     idx += 1




# range()
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified number.
# range(start?, stop, step?)


seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])

# for i in range(10): # range(stop)
#     print(i)


# for i in range(2,10): # range(start,stop)
#     print(i)


# for i in range(2,10,2): # range(start,stop, step) # excluded stop
#     print(i)


# for i in range(100,0,-1): # range(start,stop, step) # excluded stop
#     print(i)








# Pass Statement
# pass is a null statement that does nothing. It is used as a placeholder for fututre code.
    
    # for el in range(10):
    # pass

# for i in range(4):
#     pass
# print("some useful work")


# write a program to find the factorial of first n numbers. (using for)

n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print("Total factorial = ", fact)