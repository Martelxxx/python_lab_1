# Input username and return:
input_username = input("What is your name: ")
print("Hello, " + input_username + "!")

# Reverse words in an array
string = ["a man, a plan, a canal, frenemies!"]
string = string[0].split()
string = string[::-1]
string = " ".join(string)
print(string)

# Swap values of two variables
a = 30
b = 20
a, b = b, a
print(a)

# Multiply all values in a list
list = [1, 2, 3, 4, 5]
product = 1
for i in list:
    product *= i
print(product)

# Fizz Buzzer: if x is divisbile by 3 return Fizz, divisible by 5 return Buzz, divisible by 3 and 5 return FizzBuzz
def fizz_buzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x
    
# Nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#  Search for a value in a list and return true or false
def search_list(list, value):
    for i in list:
        if i == value:
            return True
    return False

# Check ifa string is a palindrome
def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
#  Check if a list has duplicates
def duplicates(list):
    for i in list:
        if list.count(i) > 1:
            return True
    return False




