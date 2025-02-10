def main():
    # Beder brugeren om at indtaste en sætning
    sentence = input("Indtast en sætning: ")

    # Åbner filen output.txt i skrive-tilstand og gemmer sætningen
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(sentence)
    print("Sætningen er gemt i output.txt")

if __name__ == "__main__":
    main()