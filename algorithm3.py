# 1. Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical
# mean. The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def arith_mean(l1):
    n = len(l1)
    sum = 0

    for i in l1:
        sum += i

    return sum/n

list1 = [1, 3, 5, 6, 4, 10, 2, 3]
print(arith_mean(list1))

# 2. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def two_lowest(l2):
    lowest = 0
    second_lowest = 0
    temp = 0
    for i in range(len(l2)-1):
        if l2[i] < lowest
            lowest = l2[i]
            second_lowest = lowest
        elif l2[i] < second_lowest
            second_lowest = l2[i]
    return l2[0], l2[1]


list2 = [198, 3, 4, 9, 10, 9, 2]
print(" ...:", two_lowest(list2))
