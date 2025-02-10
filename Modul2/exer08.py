def main():
    library = {
        "authors": ["Arthur Conan Doyle", "Isaac Asimov"],
        "books": [("Sherlock Holmes", "Fiction"), ("Foundation", "Science Fiction")],
        "available": {"Sherlock Holmes": 5, "Foundation": 2}
    }
    print(library["books"][1][1])
    library["available"]["Sherlock Holmes"]=library["available"]["Sherlock Holmes"]-1
    print(library)

if __name__ == "__main__":
    main()