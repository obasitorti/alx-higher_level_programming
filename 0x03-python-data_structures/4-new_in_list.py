def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        i = my_list.copy()
        i[idx] = element
        return (i)
