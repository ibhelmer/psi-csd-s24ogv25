# Sure! Here's a simple Python program that checks if the given string is a palindrome:
# This program first cleans the input string by removing any characters that aren't letters or numbers and converting everything to lowercase.
# This allows the program to identify palindromes that have spaces, punctuation, or mixed case, like "A man, a plan, a canal, Panama!". After cleaning, it checks if the string reads the same forward and backward.
def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned_s == cleaned_s[::-1]

def main():
    user_input = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print("True: The string is a palindrome.")
    else:
        print("False: The string is not a palindrome.")

if __name__ == "__main__":
    main()
