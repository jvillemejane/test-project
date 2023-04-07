#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:12:59 2023

@author: Julien Villemejane - LEnsE / IOGS / Palaiseau
"""

from matplotlib import pyplot as plt
import numpy as np


def my_first_function(param1, param2):
    '''
    Returns the product of param1 and param2

    Parameters
    ----------
    param1 : float
        First term of the multiplication.
    param2 : float
        Second term of the multiplication.

    Returns
    -------
    float
        Product of param1 and param2.

    '''
    return param1 * param2


if __name__ == '__main__':
    print("This is a python package/module")