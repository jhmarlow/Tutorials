# 3.1 FizzBuzz
def FizzBuzz():
# Create empty array
    result = []
    for num in range(1, 100):
# Create default ans
        add = ''
        if num % 3 == 0:
            add += 'Fizz'
        if num % 5 == 0:
            add += 'Buzz'
        if add == '':
            result.append(num)
        else:
            result.append(add)
    return result

print(FizzBuzz())


# 3.2 Two sum problem returns true if any add to S
def twoSum(array, sum):
    hashtable = {}
    for i in range(0, len(array)):
        # Calculate what to look for
        sumMinusElement = sum - array[i]
        if sumMinusElement in hashtable:
            return True
        hashtable[array[i]] = True
    return False

# Create random array
import numpy
RA = numpy.random.randint(10, size=(4, 10))
RA = RA.flatten()

print(twoSum(RA, 10))

# 3.3 Sum nested arrays

A = [1, 1, 1, [3, 4, [8]], [5]]

def sumnested(arr):

    result = 0

    # sum up numbers in array
    for i in range(0, len(arr)):

        # if nested array it will return list and therefore start function again
        if type(arr[i]) is not int:
            result += sumnested(arr[i])
        else:
            result += arr[i]
    return result


print(sumnested(A))


# 3.4 Calculate angle on a clock

def handangle(hour, minute):
    totalangle = 360
    totalhours = 12
    totalminutes = 60

    hourhandangle = hour*(totalangle/totalhours)+(minute/totalminutes)*totalangle/totalhours
    minutehandangle = minute*(totalangle/totalminutes)
    diffhandangle = abs(hourhandangle - minutehandangle)

    if diffhandangle > 180:
        diffhandangle = diffhandangle - 180

    return(hourhandangle, minutehandangle, diffhandangle)

print(handangle(2, 5))

# 3.5 Determine if N is a prime number

def isprime(N):

    if N < 2:
        return False

    for i in range(2, N):
        if N % i == 0:
            return False
        else:
            return True


print(isprime(6))


# 3.6 Create mapping function

def map(arr, fn):

    result = []

    for i in arr:
        applied = fn(i)
        result.append(applied)

    return result

def square(x):
    ans = x * x
    return ans

def addzeros(x):
    return int(str(x) + '0000')

print(map([1,2,3,4], addzeros))


# 3.6 Create filter

def filter(arr, fn):

    result = []

    for i in arr:
        if fn(i) == True:
            result.append(i)
    return result

isPositive = lambda x: x > 0

print(filter([1,2,-1,2,-2,3], isPositive))

# 3.7 Remove characters from a string

def removechar(arr, string):

    # stores letters as true in hashtable
    hashtable = {}
    for c in arr:
        hashtable[c] = True

    # create new string
    result = ''
    # Search through and print letters not there
    for i in string:
        if i not in hashtable:
            result += i
    return result

print(removechar(['h','e','w','o'], 'hello world'))

# 3.8 Check bracket count

def bracketcount(str):

    counterr = 0
    counterl = 0

    for i in str:
        if i == '(':
            counterr += 1
        elif i == ')':
            counterl += 1

    print(counterr, counterl)

    if counterr == counterl:
        return True
    else:
        return False

print(bracketcount('())'))

# 3.9 First non-repeating character

def firstNR(str):

    hashtable = {}

    for c in str:
        hashtable[c] = True

    for i in str:
        if i not in hashtable:
            print(i)

firstNR('hello henry')

# 3.10


def threeVowels(str):
    # split the list
    arr = str.split(' ')
    count = 0





str = 'We are going to go with the second method of using a regular expression (regex) to count the vowels in a word and determine whether they are continuous. '

