input_file = input("Enter the input file's name: ")
open_file = open(input_file, "r")
try:
    contents = open_file.read()

    letter_value = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,\
                    'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,\
                    'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,\
                    's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,\
                    'y': 0, 'z': 0}

    def count(contents):
        histogram = letter_value
        for l in contents:
            try:
                histogram[l.lower()] += 1
            except KeyError:
                pass
            except ValueError:
                pass
        return histogram

    for letter, l in count(contents).items():
        if l > 0:
            print('{} -> {}'.format(letter, l))
finally:
    open_file.close()
