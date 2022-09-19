def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[x]), end='')
            c += 1
        except (IndexError, ValueError):
            continue
    # print()
    return (c)
