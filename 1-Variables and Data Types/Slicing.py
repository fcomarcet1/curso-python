#SLICING
#Slicing is a powerful technique in Python that allows you to extract a portion of a sequence, such as a string, list, or tuple. The syntax for slicing is as follows:
#sequence[start:stop:step]
#start: The index where the slice begins (inclusive).
# stop: The index where the slice ends (exclusive).
# step: The interval between elements in the slice (optional, default is 1).   

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1]) # d

print(my_str[1:4]) # ell
print(my_str[8:])  # rld
print(my_str[:7])  # Hello w

print(my_str[:])  # Hello world

#string[start:stop:step]
print(my_str[0:11:2])  # Hlowrd
print(my_str[::2])  # Hlool
print(my_str[1::2]) # el wrd
print(my_str[::-1]) # dlrow olleH
