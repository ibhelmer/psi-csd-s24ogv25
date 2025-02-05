# Here's a simple Python program that creates a file named file1.txt and writes the specified string to it:
# When you run the program, it will create the file file1.txt in the current directory and write the given text into it. Using the with statement ensures that the file is properly closed after writing.
def main():
    # Open the file for writing
    with open("file1.txt", "w") as file:
        file.write("Monty Python and the Quest for the Holy Grail")

    print("Text has been written to file1.txt!")

if __name__ == "__main__":
    main()