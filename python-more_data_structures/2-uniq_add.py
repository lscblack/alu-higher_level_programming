#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = list()
    for item in my_list:
        if item not in uniq_list:
            uniq_list.append(item)
    return sum(uniq_list)
