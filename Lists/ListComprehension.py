names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Pythonic way of looping over list uses list comprehension. Note that lists are ordered collections of items or objects. This makes lists in Python 
# "sequence types", as they behave like a sequence. This means that they can be iterated using for loops. Other examples of sequences are Strings, 
# tuples, or sets.  Lists are similar in spirit to strings you can use the len() function and square brackets [ ] to access the data, with the first
# element indexed at 0.

# loop over the contents of names 
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# Print the list created by using list comprehension
best_list = [name.upper() for name in names if len(name) >= 6]
print(best_list)

MyNumbers = [1, 2]
S = [x**2 for x in MyNumbers]
print(S)