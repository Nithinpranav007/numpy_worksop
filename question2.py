# find if the given number is a palindrome or not?
# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert the number to a string
    str_number = str(number)
    # Check if the string is the same forwards and backwards
    if str_number == str_number[::-1]:
        return "The number {} is a palindrome.".format(number)
    else:
        return "The number {} is not a palindrome.".format(number)

# Example usage
number = int(input("Enter a number: "))
result = is_palindrome(number)
print(result)
