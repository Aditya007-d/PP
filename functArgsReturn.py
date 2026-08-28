#Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last"

firstName = str(input("Enter your first name "))
lastName = str(input("Enter your last name "))

def full_name(firstName, lastName):
    print (firstName, lastName)
full_name(firstName, lastName)



#Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

#Both length and width
#Only length (use default width)

length = float(input("Enter the legth of the plot "))
width = float(input("Enter the width of the plot "))

def area(length, width):
    return length*width

print(area(length, width))