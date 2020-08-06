#!/usr/bin/python
#-*-coding: utf8-*-


def quick_sort(l_in:list)->list:
    if len(l_in) <= 1:
        return l_in
    l_left = []
    l_right = []
    axis = l_in[0]
    for i in l_in[1:]:
        if i < axis:
            l_left.append(i)
        else:
            l_right.append(i)
    l_out = quick_sort(l_left) + [axis] + quick_sort(l_right)
    return l_out

if __name__ == "__main__":
    print(quick_sort([4,5,89,5,7]))