# List are mutable, ordered, and indexed collection of items.
# List can contain items of different types.
# List are created using square brackets [].
# List can be created using list() constructor.

l1 = list()
l2 = [1, 5, 10, 15, 20]

l3 = [1, 72, 31, 4, 5, 31]
print(l3)

print(l3.index(31)) # returns the index of the first occurrence of the value
print(l3.index(31, 2)) # returns the index of the first occurrence of the value starting from the index 2

l3.append(100) # adds an item to the end of the list
print(l3)

l3[1] = 50 # updates the value at the index 1
print(l3)

l3.insert(2, 200) # adds an item at the index 2
print(l3)

l3.remove(31) # removes the first occurrence of the value
print(l3)
l3.remove(31) # removes the first occurrence of the value
print(l3)

l4 = [1, 2, 3]
print(l4.pop()) # removes the last item and returns it
print(l4)
l4.clear() # removes all the items
print(l4)

l3.sort() # sorts the list
print("l3", l3)

print(l3.count(100)) # returns the number of occurrences of the value

print(l3[1:4])

l6 = l3.copy()
print("l6", l6)

l6[1] = 10
print("l3", l3)
print("l6", l6)
