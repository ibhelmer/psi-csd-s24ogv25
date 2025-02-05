# Here's a Python program that follows the mentioned instructions:
# This program first prompts the user to specify the number of words they want to add. Then, it opens file2.txt for writing and asks the user to input the specified number of words, writing each word to a new line in the file. Finally, it opens the file for reading and prints each line to the console.
def main():
    # Ask user for the number of words to add
    num_words = int(input("How many words would you like to add? "))

    # Open file2.txt for writing
    with open("file2.txt", "w") as file:
        for _ in range(num_words):
            word = input(f"Enter word {_+1}: ")
            file.write(word + '\n')

    print("\nContent of file2.txt:")

    # Open file2.txt for reading and print its contents
    with open("file2.txt", "r") as file:
        for line in file:
            print(line.strip())  # strip() is used to remove trailing newline characters

if __name__ == "__main__":
    main()