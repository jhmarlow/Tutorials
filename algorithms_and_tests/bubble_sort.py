import time
# Bubble sort algorithm in Python
list_of_numbers = [3, 54, 6575, 34, 646, 4]
tic = time.clock()
# init status
status = 0

# while the list has been sorted, resort
while status < len(list_of_numbers)-1:
    status = 0  # re initialise count
    for index in range(0, len(list_of_numbers)-1):  # loop through list
        # if numbers need to be swapped
        if list_of_numbers[index] > list_of_numbers[index+1]:
            list_of_numbers[index], list_of_numbers[index+1] = \
                list_of_numbers[index+1], list_of_numbers[index]  # swap
        else:
            status += 1
    # display progress
    print(list_of_numbers)
    print(status)

print("Success!")
print(list_of_numbers)
toc = time.clock()
print(tic-toc)



# Bubble sort algorithm in Python
list_of_numbers = [3, 54, 6575, 34, 646, 4]
tic1 = time.clock()
for i in range(0, len(list_of_numbers)-1):
    for j in range(0, len(list_of_numbers)-1-i):
        if list_of_numbers[j] > list_of_numbers[j+1]:
            list_of_numbers[j], list_of_numbers[j+1] \
                = list_of_numbers[j+1], list_of_numbers[j]

    # display progress
    print(list_of_numbers)
    print(status)

print("Success!")
print(list_of_numbers)
toc1 = time.clock()
print(tic1-toc1)
