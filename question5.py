#write a program to find if the given number is prime no or not
# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print("The number {} is a prime number.".format(number))
else:
    print("The number {} is not a prime number.".format(number))
