# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:29:51 2019

@author: smcdeid
"""

import os
from arcpy.da import Walk

class Gdbcat:
    def __init__(self, path=None):
        self.path = path
        
        if not path:
            self.path = 'blah blah blah'