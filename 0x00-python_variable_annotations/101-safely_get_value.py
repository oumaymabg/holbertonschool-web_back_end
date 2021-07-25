#!/usr/bin/env python3
'''
Module that annotates a function's parameters and return types accordingly
'''
from typing import TypeVar, Union, Mapping, Any


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar('T'),
                     None] = None) -> Union[Any, TypeVar('T')]:
    '''
    Function that returns the elements of a list type-annotated
    '''
    if key in dct:
        return dct[key]
    else:
        return default
