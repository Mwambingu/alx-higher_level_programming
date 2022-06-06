#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        f_char = None
        s_len = 0
    else:
        f_char = sentence[0]
        s_len = len(sentence)

    tuple_sen = (s_len, f_char)
    return tuple_sen
