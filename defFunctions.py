total_num = int(input("Select the quantity of numbers"))

i = 0
sum = 0
while(i<total_num):
    i = i + 1
    take_num = int(input("Enter the number"))
    sum = sum + take_num

def average(total_num, sum):
    avg = (sum)/total_num
    return avg

o1 = print(average(total_num, sum))


#Write a function greet() that prints "Hello, Python Learner!" when called.

def greet():
    return "Hello, Python enthusiasts"
print(greet())

#Write a function square(num) that returns the square of a given number. Test it with different numbers.

def square(a):
    return a**2
print(square(4))

