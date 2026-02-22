greeting = 'Hello' + 'World'
print(greeting) # Output: HelloWorld    

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
print(full_name) # Output: John Doe 

number1 = '10'
number2 = '20'
result = number1 + number2
print(result) # Output: 1020 (string concatenation, not addition)



# augmented assignment operator ,+=. This is shorter than writing var = var + 'new text'.
#Remember that strings are immutable, therefore this operation does not change the original string. Instead it creates a new string and reassigns it to the variable.
greeting = 'Hello'
greeting += ' World'
print(greeting) # Output: Hello World

address = '123 Main Street'
address += ', Apartment 4B'  
print(address) # Output: 123 Main Street, Apartment 4B

# To perform addition, we need to convert the strings to integers
result = int(number1) + int(number2)
print(result) # Output: 30 (integer addition)


my_num = str(42)
print(type(my_num)) # <class 'str'>

employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)


name = 'John'
print(f'Hello {name}') # Output: Hello John


first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
employee_card = f'Employee: {full_name}'
print(employee_card)


employee_age = 28
employee_card = f'Employee: {full_name} | Age: {employee_age}'

#extract a specific portion of a string. This is called slicing.
#The syntax is string[start:stop], where:

#start is the index where the slice begins (inclusive).
#stop is the index where the slice ends (exclusive).
#For example, if text = 'Python', then text[0:2] gives 'Py'.
text = 'Python Programming'
print(text[0:6]) # Output: Python
print(text[7:18]) # Output: Programming


#To get the last three characters of a string, you can use string[-3:]
print(text[-3:]) # Output: ing