# Here's a simple Python program that asks the user for two numbers as input, and then divides the first number with the second:
# However, keep in mind that if the user enters 0 for the second number, attempting to divide by zero will raise an error. Therefore, it's a good practice to include error handling for such cases.
def main():
    try:
        # Ask the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Check for division by zero
 #       if num2 == 0:
 #           print("Error: Division by zero is not allowed.")
 #           return

        # Divide and print the result
        result = num1 / num2
        print(f"\nResult of {num1} divided by {num2} is: {result}")

    except ZeroDivisionError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()