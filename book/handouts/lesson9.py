# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:18:46 2023

@author: george.york
"""
# code from lesson 9
# by George York

# estimating comp time for DFT versus FFT
# assume DFT has initial overhead of 5 ops and FFT has initial overhead of 20 ops

# import libraries
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# n=1:8;
n = np.arange(1,9) 
plt.plot(n, n*n + 5, n, n*np.log2(n) + 20);

#n=1:64;
n = np.arange(1,65) 
plt.plot(n, n*n + 5, n, n*np.log2(n) + 20);

#n=1:1024;
n = np.arange(1,1025)
plt.plot(n, n*n + 5, n, n*np.log2(n) + 20);

# 4 point FFT
#x = [0 1 1 0]
x = np.array([0.0, 1.0, 1.0, 0.0])
print("time domain input", x)
print("FFT of input     ",np.abs(np.fft.fft(x)))

