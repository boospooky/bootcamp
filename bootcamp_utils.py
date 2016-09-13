'''
bootcamp_utils: A collection of statistcal functions
proved useful 55 students
'''

import numpy as np


def ecdf(data):
    '''
    Compute x, y values for an empirical distribution
    function
    '''
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y
