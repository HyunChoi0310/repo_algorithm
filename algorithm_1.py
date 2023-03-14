#1.Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
#Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def sum_of_n(n: int):
    result = 0
    for i in range(1, n+1):
        result = result + i

    print(f'Result : {result}')

sum_of_n(5)

#Find the max number from 3 values.
#Example: 124, 21, 32. Result = 124.
def max_number_from_3(a: int, b: int, c: int):
    temp = a
    if b > temp:
        temp = b
    elif c > temp:
        temp = c

    print(f'MAX numer is  {temp}')

max_number_from_3(111, 5, 300)

#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5)
def even_odd(n: str):
    even_count = 0
    odd_count = 0
    for i in n:
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f'Even_count {even_count}, Odd_count {odd_count}')

even_odd("12345")



