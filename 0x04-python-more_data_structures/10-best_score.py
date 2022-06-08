#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    else:
        value = list(a_dictionary.values())
        key = list(a_dictionary.keys())
        return (key[value.index(max(value))])
