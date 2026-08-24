'''Take the string "  i love python programming  " and:

Remove extra spaces from both ends
Convert it to title case
Count how many times "o" appears'''

text = "  i love python programming  "
print(text.strip(), text.title(), text.count("o"))


#Check if the string "123abc" is alphanumeric.
str1 = "123abc"
print(str1.isalnum())