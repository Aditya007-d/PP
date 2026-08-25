#Write a program that counts how many vowels are in a given string.

text = "Python programming is nice"
c1 = text.count("a")
c2 = text.count("e")
c3 = text.count("i")
c4 = text.count("o")
c5 = text.count("u")

print(c1 + c2 + c3 + c4 + c5)

###################################################################

sum = 0
vowel = ["a", "e", "i", "o", "u"]
for char in text.lower():
    if(char in vowel):
        sum = sum + 1
print(sum)


########################################################
#Take a user input string and check if it is a palindrome (same forwards and backwards).

input1 = str(input("Enter your string input"))
input2 = input1.lower()

if(input2 == str(input2)[::-1]):
    print("Input string is palindrome")
else:
    print("Not Palindrome")