#!/usr/bin/env python3
'''
Module that takes a mixed list of floats and integers and returns the sum as
float
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Type-annotated function that takes a mixed list of floats and integers and
    returns the sum as float
    @mxd_lst: the mixed list
    Return: the sum of the mixed list as float
    '''
    res = 0
    for num in mxd_lst:
        res += num

    return res
