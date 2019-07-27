# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:09:14 2019

@author: arnou
"""

import datetime as dt
import hashlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import unittest
import uuid

class Block:
    def __init__(self,previous_block_hash, data, timestamp):
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()
    
    def get_hash(self):
        header_bin = (str(self.previous_block_hash) + str(self.data) + str(self.timestamp)).encode()
        
        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

        