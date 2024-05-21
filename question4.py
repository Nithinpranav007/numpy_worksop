#write a program to find the sum of digits of a given number'
# Function to calculate the sum of digits of a number
def sum_of_digits(number):
    # Initialize the sum to 0
    total = 0
    # Convert the number to positive if it is negative
    number = abs(number)
    # Loop through each digit in the number
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

# Example usage
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("The sum of the digits of {} is {}.".format(number, result))
