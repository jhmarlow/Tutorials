houses = ["Erics house", "Kennys house", "Kyle's house", "Stan's house"]


def santa_delivering_iteratively():
    for house in houses:
        print("Delivering to", house)

print("iterative method")
santa_delivering_iteratively()


def santa_deliver_recursively(houses):

    if len(houses) == 1:
        house = houses[0]
        print("Delivering to", house)
    else:
        mid = len(houses)//2
        first_half = houses[:mid]
        second_half = houses[mid:]
        # back into function (recursion)
        santa_deliver_recursively(first_half)
        santa_deliver_recursively(second_half)


print("recursive method")
santa_deliver_recursively(houses)


def factorial_recursive(n):
    # base case if this is met: factorial_recursive(n-1) = 1
    if n == 1:
        return 1
    else:
        # Go into the recursion
        return n * factorial_recursive(n-1)


print("Factorial recursive")
print(factorial_recursive(5))


def sum_list(list):
    if list == []:
        return 0
    else:
        head_of_list = list[0]
        smaller_list = list[1:]
        return head_of_list + sum_list(smaller_list)


print(sum_list([1, 2, 3]))




def fibonacci(n):
    # base case
    print("\nCalculating F", "(", n, ")", sep="", end=", " )
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(5))