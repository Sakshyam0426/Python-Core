# Functions — def, parameters, return
# Prime Check — Check if a number is divisible by another using % (modulo) operator
# Factorial — multiplying in a loop
# Fibonacci — two-variable swapping a, b = b, c
# String traversal — checking characters 
# List separation — splitting into even/odd
# Linear Search — finding a value index by index
# Sum of digits — using % 10  
# String reversal — looping backwards range(n-1, -1, -1)
# List stats — sum, average, max, min manually




# Check if a number is prime
def is_prime(num):
    count = 0                        # counts how many numbers divide num
    for i in range(1, num):          # loop from 1 to num-1
        if num % i == 0:             # if i divides num with no remainder
            count += 1              
    if count > 1:                   
        return False                 # more than 1 divisor = not prime
    return True                      # only 1 divisor = prime

result = is_prime(23)
if result is True:
    print(f"Number is prime")
else:
    print(f"Number is not prime")


# Factorial using loop
def factorial(n):
    result = 1                       # start from 1 (not 0, multiplying by 0 = 0)
    for i in range(1, n+1):          # loop from 1 to n
        result = result * i          # multiply each number: 1x2x3x4...
    return result                   

fact = factorial(4)
print(f"Factorial: {fact}\n")


# Fibonacci series up to x terms
def fibonacci(n):
    a = 1                            
    b = 1                           
    print(f"{a} {b}", end=" ")       
    for i in range(n-2):             # loop remaining terms (n minus first 2)
        c = a + b                    
        print(c, end=" ")            
        a, b = b, c                  # shift forward: a gets b, b gets c

print(f"Fibonacci series of 10 terms: ", end=" ")
fibonacci(n=10)
print("\n")


# Check a string for uppercase letters
def uppercase(s):
    result = ""                                # empty string to store uppercase letters
    for char in s:                             # loop each character
        if char >= 'A' and char <= 'Z':        # A=65, Z=90, checks ASCII range
            result = result + char             # add uppercase char to result
    return result                            

string = "LICT STUDENT"
uppercase_string = uppercase(string)
print(f"Uppercase letters: {uppercase_string}\n")


# Construct a list of even and odd numbers
def even_odd_list(numbers: list):
    length_of_list = len(numbers)    # get total length of list
    even_numbers = []                # empty list for even numbers
    odd_numbers = []                 # empty list for odd numbers

    for i in range(length_of_list):
        if numbers[i] % 2 == 0:                              # remainder 0 = even
            even_numbers.append(numbers[i])
        else:                                                # remainder 1 = odd
            odd_numbers.append(numbers[i])

    return even_numbers, odd_numbers                         # return both lists

numbers = list(range(1, 21))
even_numbers_list, odd_numbers_list = even_odd_list(numbers)
print(f"Even Numbers List: {even_numbers_list}")
print(f"Odd Numbers List: {odd_numbers_list}\n")


# Search for a target value in a list (Linear Search)
def search(numbers, target):
    length_of_list = len(numbers)                                  # get total length of list
    for i in range(length_of_list):
        print(f"Checking index {i} with value: {numbers[i]} ...")
        if numbers[i] == target:                                   # if current value matches target
            return i                                               # return the index where found
    return -1                                                      # -1 means target not found

def main():
    numbers = [3, 5, 9, 12, 17, 2, 1, 6, 8, 4]
    target = 4
    result = search(numbers, target)
    if result != -1:                                                  # -1 means not found
        print(f"Target ({target}) found in list at index {result}\n")
    else:
        print("Target not found in the list.")
main()


# Sum of digits of a number
def sum_of_digits(number):
    result = 0                       # stores sum of digits
    while number != 0:               # loop until all digits are processed
        remainder = number % 10      # grabs last digit (67 % 10 = 7)
        result = result + remainder  # add last digit to result
        number = number // 10        # remove last digit (67 // 10 = 6)
    return result                    # 67 -> 7+6 = 13

number = 67
result = sum_of_digits(number)
print(f"The sum of digits of number {number} is: {result}\n")


# Manually reverse a string
def reverse(word):
    length_of_string = len(word)                    # get length of string
    reversed_string = ""                            # empty string to build reverse
    for i in range(length_of_string - 1, -1, -1):   # loop backwards
        reversed_string += word[i]                  # add each char from end to start
    return reversed_string                          # "reverse" -> "esrever"

word = "reverse"
print(f"The reverse of {word} is: {reverse(word)}\n")


# Calculate sum, average, maximum and minimum
def calculate(numbers):
    total = 0                        # stores total sum
    maximum = numbers[0]             # assume first number is max
    minimum = numbers[0]             # assume first number is min

    for num in numbers:
        total += num                 
        if num > maximum:            # if current num is bigger
            maximum = num            # update maximum
        if num < minimum:            # if current num is smaller
            minimum = num            # update minimum

    average = total / len(numbers)   # total divided by count

    return total, average, maximum, minimum

numbers = [1, 2, 3, 4, 5]
total, average, maximum, minimum = calculate(numbers)
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}\n")