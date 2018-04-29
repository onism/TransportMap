import sys
import logging
import os.path
import dill

__all__ = ['TMO']

class TMO(object):
    """Base object for every object in the module"""
    def __init__(self):
        self.set_logger()

    def set_logger(self):
        pass
