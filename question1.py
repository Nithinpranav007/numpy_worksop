# write a python code to find if the given number is odd or even?
# Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "The number {} is even.".format(number)
    else:
        return "The number {} is odd.".format(number)

# Example usage
number = int(input("Enter a number: "))
result = check_odd_even(number)
print(result)
