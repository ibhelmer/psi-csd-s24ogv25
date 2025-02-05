# Here's a Python program that prompts the user for input and then removes all periods and commas from the given string:
# You can run this program, and it will ask you to enter two numbers. After entering the numbers, it will print out the sum in the specified format.
def main():
    # Get the two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum
    total = num1 + num2
    # Print the result
    print(f"The sum of {num1} and {num2} is {total}.")

if __name__ == "__main__":
    main()