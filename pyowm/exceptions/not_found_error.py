#!/usr/bin/env python

"""
Module containing NotFoundError class
"""

from os import linesep

class NotFoundError(Exception):
    """
    Error class that represents the situation when an entity is not found into
    a collection of entities.
    
    :param cause: the message of the error
    :type cause: str
    :returns: a *NotFoundError* instance
    """    
    def __init__(self, message):
        self._message = message
        
    def __str__(self):
        """Redefine __str__ hook for pretty-printing"""
        return ''.join(['The searched item was not found.', linesep, 'Reason: ', \
            self._message])