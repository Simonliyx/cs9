import sys

def usage():
    print("USAGE: welcome.py characters replacements")
    sys.exit(1)

def main():

    if len(sys.argv) != 3:
        usage()

    chars = sys.argv[1]
    replacements = sys.argv[2]


    if len(chars) != len(replacements):
        print("ERROR: Arguments must be the same length.")
        sys.exit(1)


    translation_table = {chars[i]: replacements[i] for i in range(len(chars))}


    for line in sys.stdin:

        translated_line = ''.join(translation_table.get(c, c) for c in line)
        print(translated_line, end='')

if __name__ == "__main__":
    main()
