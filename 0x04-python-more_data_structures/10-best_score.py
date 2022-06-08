#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_score = 0
    best_scorer = ""
    for k, v in a_dictionary.items():
        if v > best_score:
            best_score = v
            best_scorer = k
    return best_scorer
