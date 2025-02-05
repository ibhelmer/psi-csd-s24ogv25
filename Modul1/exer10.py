# Here's a Python program that accepts city names from the user and appends them to a list. The user can signal that they're done entering names by simply pressing enter without typing anything:
# When you run the program, you can keep adding city names. Once done, just press Enter, and the program will display the list of entered city names.
def main():
    cities = []
    while True:
       city = input("Enter a city name (press enter to stop): ")

       if not city:  # Check if the user entered an empty string
           break

       cities.append(city)

# Print the cities
    print("\nList of entered cities:")
    for city in cities:
        print(city)

if __name__ == "__main__":
    main()

