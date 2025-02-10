def transformfile ():
    try:
        with open("input.txt", 'r', encoding='utf-8') as infile, open("transformed.txt", "w", encoding="utf-8") as outfile:
            lines = infile.readlines()
            for line in lines:
                l = len (line)
                oline=line[::-1]
                outfile.write(oline+','+str(l))
    except FileNotFoundError:
        print(f'Filen "{filename}" blev ikke fundet.')
    except Exception as e:
        print(f'Der opstod en fejl: {e}')

def main():
    transformfile()

if __name__ == "__main__":
    main()