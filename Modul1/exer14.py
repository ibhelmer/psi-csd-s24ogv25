# If you try to open a non-existing file for reading, Python will raise a FileNotFoundError. To handle this gracefully, we can use a try-except block.
# Let's write a program to open file1.txt and add the text "Life of Brian" to it:
# Here's what the program does:
#   1) It tries to open file1.txt in append mode. If the file exists, the program will simply add the new text to the end of the file. If the file doesn't exist, it will raise a FileNotFoundError.
#   2) If a FileNotFoundError is encountered, the program will print an error message stating that the file was not found.
def main():
    try:
        # Open the file in append mode to add text without overwriting existing content
        with open("file1.txt", "a") as file:
            file.write("\nLife of Brian")

        print("Text 'Life of Brian' has been added to file1.txt!")

    except FileNotFoundError:
        print("Error: file1.txt was not found.")

if __name__ == "__main__":
    main()