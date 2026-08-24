'''Using format(), create a sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables.'''

text = "My name is {} and I am {} years old."
t1 = text.format("John", "25")
print(t1)

#Do the same using f-strings. 

name = "John"
age = "25"
print(f"My name is {name} and I am {age} years old")