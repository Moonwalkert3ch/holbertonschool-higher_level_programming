#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_sum = []

    for i in my_list:
        if i % 2 == 0:
            list_sum.append(True)
        else:
            list_sum.append(False)
    return (list_sum)
