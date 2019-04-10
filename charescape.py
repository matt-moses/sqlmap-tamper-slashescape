#!/usr/bin/env python

"""
Copyright (c) 2019 Matthew Moses
See the file 'LICENSE' for copying permission
"""

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Escapes a char encoded payload

    Tested against:
        * This is just a proof of concept but used for sqlinjection against MySQL 5.7.25

    Notes:
        * Useful when passing a payload as a string via a JSON context

    >>> tamper('\u0022')
    '\\u0022'
    """

    retVal = payload

    if payload:
        retVal = retVal.replace("\\", "\\\\")

    return retVal
