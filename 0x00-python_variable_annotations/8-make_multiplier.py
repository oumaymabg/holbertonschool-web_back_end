#!/usr/bin/env python3
'''
Module that takes a a float as argument and returns a function that multiplies
a float by the previous float
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Type-annotated function that takes a a float as argument and returns a
    function that multiplies a float by the previous float
    @multiplier: the float that will be returned in the function
    Return: a fucntion that multiplies a float by multiplier
    '''
    def multiply_by(num: float) -> float:
        '''
        Function that multiplies num by multiplier and returns a float
        @num: the number to multiply
        Return: the multiplication of the two floats as float
        '''
        return num * multiplier

    return multiply_by
