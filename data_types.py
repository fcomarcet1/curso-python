#INTEGER
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10

#FLOAT
my_float_var = 4.50
print('Float:', my_float_var) # Float: 4.5

#STRING
my_string_var = 'Hello, Python!'
print('String:', my_string_var) # String: Hello, Python!

#BOOLEAN
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True

#SET: unordered collection of unique elements in  curly braces
my_set_var = {1, 2, 3, 4, 5}
print('Set:', my_set_var) # Set: {1, 2, 3, 4, 5}

#DICTIONARY: A collection of key-value pairs in  curly braces
my_dict_var = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print('Dictionary:', my_dict_var) # Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}

#TUPLE: IMMUTABLE ordered collection of elements in parentheses
my_tuple_var = (1, 2, 3, 4, 5)
print('Tuple:', my_tuple_var) # Tuple: (1, 2, 3, 4, 5)

my_tuple_var2 = (1, 'Hello', 3.14, True)
print('Tuple:', my_tuple_var2) # Tuple: (1, 'Hello', 3.14, True)

#RANGE: A sequence of numbers, often used in loops,
my_range_var = range(5)
print('Range:', my_range_var) # Range: range(0, 5)

my_range_var2 = range(0, 10)
print('Range:', my_range_var2) # Range: range(0, 10)

#lIST: An ordered collection of elements that supports different data types.
my_list_var = [1, 'Hello', 3.14, True]
print('List:', my_list_var) # List: [1, 'Hello', 3.14, True]

#NONE:A special value that represents the absence of a value(similar to null in other languages)
my_none_var = None
print('None:', my_none_var) # None: None    

#GET DATA TYPE: Use the type() function to check the data type of a variable
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 5, 8}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 5, 8)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>

#IS INSTANCE: Check if a variable is of a specific data type returns True or False
isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False