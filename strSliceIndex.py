'''Given text = "Python Programming", do the following:

Print the first 6 characters
Print the last 6 characters
Print every second character from the string'''

text = "Python Programming"
print(text[:6], text[-6:], text[0::2])

#Reverse the string text using slicing.

print(str(text)[::-1])