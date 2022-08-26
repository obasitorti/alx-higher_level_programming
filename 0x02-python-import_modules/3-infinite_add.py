#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg = argv[1:]
    sum = 0
    if len(arg) > 0:
        for m in range(len(arg)):
            sum += int(arg[m])
        print('{}'.format(sum))
