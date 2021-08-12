from sys import argv as arguments
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = '5:DFGH["JKL;ZX/.CVBNM<>?=+'

if len(arguments) != 3:

    print("2 arguments required!")
    exit()


from_filename = arguments[1]
to_filename = arguments[2]
print("imput " +from_filename)
print("output: " + to_filename)
from_file = open(from_filename, 'r', encoding='utf8')
to_file = open(to_filename, 'w', encoding='utf8')

contents =list(from_file .read())

for index in range(len(contents)):
    letter = contents[index]
    order = ord(letter) - ord('A')
    if order < 0 or order >= len(KEY):
        continue
    cipher_letter = KEY[order]
    contents[index] = cipher_letter






to_file.write(''.join(contents))

from_file.close()
to_file.close()
