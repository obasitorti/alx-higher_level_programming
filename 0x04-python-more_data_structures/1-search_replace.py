#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # def rrplace(i):
    #     return i if i != search else replace
    # return list(map(rrplace, my_list))
    new = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            new.append(replace)
        else:
            new.append(my_list[i])
    return new
