import random

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor
    return elements

elements = []
for i in range(100):
    elements.append(random.randint(0, 500))
print(insertion_sort(elements))
