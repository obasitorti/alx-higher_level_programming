#!/usr/bin/python3
from sys import argv
__name__ == "__main__"


k = len(argv) - 1
if k == 0:
    print(k, "arguments.")
elif k == 1:
    print(k, "argument:")
    print("{}: {}".format((k), argv[1]))

elif k > 1:
    print(k, "arguments:")
    for i in range(0, len(argv[1:])):
        print("{}: {}". format(i+1, (argv[i + 1])))
