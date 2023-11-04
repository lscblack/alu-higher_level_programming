#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        sentence_length = len(sentence)
    else:
        sentence_length = 0
    return tuple((sentence_length, None if not sentence else sentence[:1]))
