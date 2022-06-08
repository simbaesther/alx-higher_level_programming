#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for sKeys in sorted(a_dictionary):
        print("{}: {}".format(sKeys, a_dictionary[sKeys]))
