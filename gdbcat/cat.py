# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:29:51 2019

@author: smcdeid
"""

import os
#import arcpy

class Gdbcat:
    def __init__(self, name):
        self.name = name
        
        if not name:
            self.name = 'blah blah blah'