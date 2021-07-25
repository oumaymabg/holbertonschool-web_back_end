#!/usr/bin/env python3
'''
Module that takes a string and an int or float and returns a tuple
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Type-annotated function that takes a string and an int or float and
    returns a tuple
    @k: the string that will be returned in the tuple
    @v: an int or float that will be squared
    Return: a tuple with k as first element and the square of v as second
    element as a float
    '''
    kv = (k, v * v)
    return kv
