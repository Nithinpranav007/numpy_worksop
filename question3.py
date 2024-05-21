#write a program to find the factorial of a nummber
# Function to calculate the factorial of a number
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result

# Example usage
number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print("The factorial of {} is {}.".format(number, result))
