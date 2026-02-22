#What Are Strings and What Is String Immutability?
#Strings are a sequence of characters. They are used to represent text in Python.
# Strings are immutable, which means that once a string is created, it cannot be changed. However, you can create a new string by concatenating two or more strings together.

#This means that you can reassign a different string to a variable
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

#But direct modification of a string isn't allowed:
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment


my_str_1 = 'Hello'
my_str_2 = "World"

#multiple lines string
my_str_3 = """Multiline
string"""

my_str_4 = '''Another
multiline
string'''

#If your string contains either single or double quotation marks, then you have two options:
#Use the opposite kind of quotes. That is, if your string contains single quotes, use double quotes to wrap the string, and vice versa:
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'


#Use of \ to escape the quotes. This allows you to include the same type of quote within the string without ending it prematurely:
msg = 'It\'s a sunny day'
quote = "She said, \"Hello World!\""

#IN FUNCTION
sentence = 'The quick brown fox jumps over the lazy dog'
print('fox' in sentence) # Output: True
print('cat' in sentence) # Output: False


#LEN FUNCTION
sentence = 'The quick brown fox jumps over the lazy dog'
length = len(sentence) # Output: 43 (including spaces)

#[] OPERATOR
my_str = "Hello world"
print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1])  # d
print(my_str[-2]) # l
