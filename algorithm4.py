# 2. Increment a Number
# Write a program that takes as input a list of digits encoding
# a nonnegative decimal integer D and updates the list to represent
# the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the
# array to [2, 3, 0].
def increment_num(lst2):
    for i in range(len(lst2) - 1):
        if lst2[i] < 9:
            lst2[i] = lst2[i] + 1
            print(lst2)
        else:
            lst2[i] = lst2[i] + 1
            print(lst2)
            lst2[i] = lst2[i] % 10
            print(lst2)
    return lst2

print(increment_num([1, 2, 9]))


# 1. Even First
# Your input is a list of integers, and you have to reorder its
# entries so that the even entries appear first. You are required
# to solve it without allocating additional storage (operate with
# the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(l):
    i = 0
    while i < (len(l) -1):
        if l[i] % 2 != 0:
            l.append(l[i])
            print(l[i])
            print(l)
            del l[i]
            i = i
            print(l)
            print(i)
    return l


print(even_first([7, 3, 5, 6, 4, 10, 3, 2]))

