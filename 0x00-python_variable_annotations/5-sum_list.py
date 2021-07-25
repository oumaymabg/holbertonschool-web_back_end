#!/usr/bin/env python3
'''
Module that takes a list of floats and returns their sum as a float
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Type-annotated function that takes a list of floats and returns its sum as
    a float
    @input_list: list of floats to sum
    Return: the sum of the list as a float
    '''
    res = 0
    for num in input_list:
        res += num

    return res
