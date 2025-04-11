# def cal_sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum

# cal_sum(1,2)
# cal_sum(13,2)
# cal_sum(1,25)


# def print_hello():
#     print("hello")

# output = print_hello()

# print(output) # None

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# # calc_avg(20,54,36)

# citied = ["London", "Paris", "New York", "Tokyo", "Berlin"]

# print(citied[0], end=" ")
# print(citied[1], end=" ")

# numbs = []

# def length_of_list(numbs):
#     count = 0
#     for i in numbs:
#      count += 1
#     return count 

# print(length_of_list(numbs))













# Recursion 
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5) # call stack
  