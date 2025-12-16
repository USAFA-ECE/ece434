# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 15:27:42 2023

@author: george.york
"""

from sampcos import sampcos
[my_x, my_Fs] = sampcos(0.1, 100, 1000)
[my_x, my_Fs] = sampcos(0.1, 100, 500)
[my_x, my_Fs] = sampcos(0.1, 100, 200)
[my_x, my_Fs] = sampcos(0.1, 100, 110);