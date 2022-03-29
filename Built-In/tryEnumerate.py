# Create new list 
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
print(type(names))

# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
print('')
print("List comprehension:")
print([(i,name) for i,name in enumerate(names)])

# Unpack an enumerate object with a starting index of one
print('')
print("Unpack Enumerate:")
print(*enumerate(names, 1))