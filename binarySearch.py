import random

numbers = []
for _ in range(100):
    numbers.append(random.randint(0, 500))

#Binary search works only on sorted lists
numbers.sort()   #TimSort O(n logn)
print(numbers)
counter = 0    #variable to check how many times the function wsa called


#If number of elements is twiced, only 1 step is added
#Searching for the existence of a numebr
def binary_search(numbers, number, left, right):
    global counter
    counter += 1
    if left > right:      #If element does nto exist
        return -1

    mid = (left + right) // 2
    if number == numbers[mid]:
        return mid
    elif number < numbers[mid]:
        return binary_search(numbers, number, left, mid - 1)
    else:
        return binary_search(numbers, number, mid + 1, right)
    

left = 0
right = len(numbers) - 1

print(binary_search(numbers, 323, left, right))   #Searching for 323
print(counter)
