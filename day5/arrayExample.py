import array

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr = array.array('i', l1)
print(arr)

# Append an element
arr.append(40)
print(arr)

# Insert element at index 1
arr.insert(1, 15)
print(arr)

# Remove element (first occurrence of 40)
arr.remove(40)
print(arr)

# Convert array to list

print(arr.tolist())
