from sys import argv as arguments
from analyze import analyze




ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if len(arguments) != 3:

    print("2 arguments required!")
    exit()


from_filename = arguments[1]
to_filename = arguments[2]
print("imput " +from_filename)
print("output: " + to_filename)
from_file = open(from_filename, 'r', encoding='utf8')
to_file = open(to_filename, 'w', encoding='utf8')

contents = from_file .read()

to_file.write(contents)

from_file.close()
to_file.close()
