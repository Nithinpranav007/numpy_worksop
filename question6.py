#write a program to find the maximum of two numbers
# Function to find the maximum of two numbers
def find_maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

maximum = find_maximum(num1, num2)
print("The maximum of {} and {} is {}.".format(num1, num2, maximum))
