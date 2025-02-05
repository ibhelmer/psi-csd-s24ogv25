# Here's a Python program that prompts the user for two integers and then prints out their sum, difference, product, and quotient:
# When you run this program, it will ask you to input two integers. After entering the numbers, the program will display their sum, difference, product, and quotient. If the second integer (b) is zero, the program will indicate that division by zero is undefined.
def main():
# Get the two integers from the user
    a = int(input("Enter the first integer (a): "))
    b = int(input("Enter the second integer (b): "))

# Calculate and print the results
    print(f"\nSum (a + b) = {a + b}")
    print(f"Difference (a - b) = {a - b}")
    print(f"Product (a * b) = {a * b}")

# Ensure that we don't divide by zero
    if b != 0:
        print(f"Quotient (a / b) = {a / b}")
    else:
        print("Quotient (a / b) = undefined (division by zero)")

if __name__ == "__main__":
    main()