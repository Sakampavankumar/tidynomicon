#!/usr/bin/env python

'''
Utilities.
'''


def report(title, values):
    '''Print values if any.'''

    if values:
        print(title)
        for v in values:
            print('  ', v)