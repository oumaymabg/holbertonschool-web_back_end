#!/usr/bin/env python3
'''
Module that annotates a function's parameters and return types accordingly
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Function that returns a list of tuples in a list
    '''
    return [(i, len(i)) for i in lst]
