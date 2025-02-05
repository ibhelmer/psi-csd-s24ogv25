# Here's a Python program that prompts the user for input and then removes all periods and commas from the given string:
# When you run this program, it will ask you for a string. After entering the string, it will print out the result with all periods and commas removed.
def remove_periods_and_commas(s):
    return s.replace(".", "").replace(",", "")

def main():
    user_input = input("Enter a string: ")
    result = remove_periods_and_commas(user_input)
    print(result)

if __name__ == "__main__":
    main()