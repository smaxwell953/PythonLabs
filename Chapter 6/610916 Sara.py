input_file = input("Enter the input file's name: ")
new_file = open(input_file + ".hist", "w+")

open_file = open(input_file, "r")
try:
    contents = open_file.read()

    #Dictionary
    letter_value = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,\
                    'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,\
                    'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,\
                    's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,\
                    'y': 0, 'z': 0}

    #Count the number of letters in the input file
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

    #Sort output based on frequency in descending order
    new_hist = dict(sorted((count(contents)).items(), key = lambda item: item[1], reverse=True))

    #Output histogram in new file with .hist
    for letter, l in new_hist.items():
        if l > 0:
            new_file.write('{} -> {}\n'.format(letter, l))

finally:
    new_file.close()
    open_file.close()
