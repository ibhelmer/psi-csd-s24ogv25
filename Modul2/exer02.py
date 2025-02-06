def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)

            for i, line in enumerate(lines, start=1):
                word_count = len(line.split())
                print(line)
                print(f'Linje {i}: {word_count} ord')

            print(f'Antal linjer i filen: {total_lines}')
    except FileNotFoundError:
        print(f'Filen "{filename}" blev ikke fundet.')
    except Exception as e:
        print(f'Der opstod en fejl: {e}')
def main():
   # Kør funktionen med data.txt
   count_words_in_file('data.txt')
if __name__ == "__main__":
    main()