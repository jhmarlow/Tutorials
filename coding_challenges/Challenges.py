# Divisible by 7 and not by 5
l = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        l.append(str(i))
print(','.join(l))

# FizzBuzz
# "Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."

for i in range(1, 100):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(str(i))

# Fibonacci
# ITERATIVE
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
a, b = 0, 1
print(a)
print(b)
for i in range(0, 10):
    num = a + b
    a = b
    b = num
    print(num)

# recursive
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

for n in range(0, 10):
print(F(n))


# Create a random array
import numpy as np
A = np.random.randint(10, size=(4, 10))
# Flatten array
AF = A.flatten()

# Find most frequent integer in an array
import numpy as np
x = np.random.randint(0, 10, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())

# Find pairs in integer array which add to 10
def sum_of_pairs_matches(K, arr):
    uniques = {i: True for i in arr}
    pairs = set()
    for val in arr:
        k = -val + K if val<K else -K - val
        if(uniques.get(k, False)):
            pairs.add(tuple(sorted([k,val])))
    return pairs


X = sum_of_pairs_matches(10, AF)
print(X)
# {(4, 6), (5, 5), (2, 8), (1, 9), (3, 7)}

target = 10
L = np.array(AF).tolist()


def find_pairs(T, array):
    index1 = []
    index2 = []
    for i1, num1 in enumerate(array):
        for i2, num2 in enumerate(array):
            if num1 + num2 == T:
                index1.append(i1)
                index2.append(i2)
                if i1 != i2:
                    print(i1, i2)

X = find_pairs(10, AF)

# Find values greater than 10
Upper = []
Lower = []
array = [2, 5, 3, 7, 5, 9, 11, 3, 5, 5, 12, 4, 6, 15]
for idx, num in enumerate(array):
    if num > 10:
        Upper.append(idx)
    elif num < 5:
        Lower.append(idx)

# Find values greater than 10 and form vector
Upper = []
Lower = []
array = (2, 5, 3, 7, 5, 9, 11, 3, 5, 5, 12, 4, 6, 15)
for num in array:
    if num > 10:
        Upper.append(1)
    else:
        Upper.append(0)
    if num < 5:
        Lower.append(-1)
    else:
        Lower.append(0)


# Remove values greater than 10 less than 5
array = [2, 5, 3, 7, 5, 9, 11, 3, 5, 5, 12, 4, 6, 15]
for idx, num in enumerate(array):
    if num > 10:
        array.remove(array[idx])
    elif num < 5:
        array.remove(array[idx])

print(array)