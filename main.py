s = input("Anna syöte: ( x = exit)")
# create character list from input
chars = list(s)
# A set can only contain unique elements. So len(set(x)) tells you the size of the set of unique elements of x.
unique_chars = len(set(chars))

print("Erilaisia merkkejä löytyi",unique_chars)