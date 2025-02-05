# Here's a Python program that takes a user's input and returns the string in the three specified formats:
# When you run this program, it will ask for a string. After entering the string, the program will print out the string in the three specified formats.
def format_string(s):
    # (a) In all caps
    all_caps = s.upper()

    # (b) In lowercase
    lowercase = s.lower()

    # (c) First word in uppercase
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    first_word_upper = ' '.join(words)

    return all_caps, lowercase, first_word_upper

def main():
    user_input = input("Enter a string: ")
    all_caps, lowercase, first_word_upper = format_string(user_input)

    print("\n(a) In all caps:", all_caps)
    print("(b) In lowercase:", lowercase)
    print("(c) First word in uppercase:", first_word_upper)

if __name__ == "__main__":
    main()