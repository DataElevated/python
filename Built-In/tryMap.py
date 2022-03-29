"""Applies a function to each object"""
MyNumberListtoRound = [1.49, 5.69381, 4.132123]
roundedMyNumberListtoRound = map(round, MyNumberListtoRound)
print(list(roundedMyNumberListtoRound))

# Create new list of names
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)

