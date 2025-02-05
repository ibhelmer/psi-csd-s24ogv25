# This is a classic coding problem known as "FizzBuzz". Here's a Python program that implements the described behavior:
# The program checks each number in the range from 1 to 100 and prints either the number itself, "Fizz", "Buzz", or "FizzBuzz" based on the conditions you provided. The end=" " argument in the print function ensures that the output is on the same line.
def main():
    for i in range(1, 101):  # Loop through numbers 1 to 100
        # Check for multiples of 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

if __name__ == "__main__":
    main()