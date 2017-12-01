# ! /usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
Testing libraries 
"""
import sys
import numpy as np

print("Die benutzten python pfade sind hier: ", sys.path)

my_test_array = np.arange(15).reshape(3, 5)

print("done", str(my_test_array))