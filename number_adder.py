# python script that adds two numbers together and prints their sum to the command line.

# Function that adds two numbers together
def add_numbers(num1, num2):
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")
    return sum

# Main function
def main():
    num1 = 5
    num2 = 10
    sum = add_numbers(num1, num2)
