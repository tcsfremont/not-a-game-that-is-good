import sys

n = int(sys.argv[1])

if n % 2 == 1:

     print("Weird")

elif n >= 2 and n <= 5:

    print("Not weird")
elif n in range(6, 21):
    print("Weird")
else:
    print("not weird")
