# Sure, here's a simple Python program that prompts the user for input three times and adds each input to a list:
# When you run this program, it will ask you to input values three times.After entering the values, the program will display the list containing the entered values.

def main():
# Create an empty list
    user_list = []

# Ask the user for input three times
    for i in range(3):
        user_input = input(f"Enter value {i + 1}: ")
        user_list.append(user_input)

# Print the list
    print("\nThe list of entered values is:", user_list)

if __name__ == "__main__":
    main()

