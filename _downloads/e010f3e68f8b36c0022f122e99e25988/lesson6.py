# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:15:43 2023

@author: george.york
"""

# demo DFT for lesson6
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from sampcos import sampcos
# this has time and freq domain plots (with fftshift built-in)
[x, Fs]=sampcos(0.005,200,4000);
# just call regular FFT
y = np.fft.fft(x)
N = len(x)
k = np.arange(0,N,1)  # goes from 0 to N-1, incrementing by 1
plt.figure(2)
plt.stem(k, np.abs(y))  # plot magnitude of regular FFT
plt.figure(3)
z = np.fft.fftshift(y)
plt.stem(k, np.abs(z))  # demo fftshift

# demo simple fft and ifft
# make an array with an impulse (one element is the value one... all others are zero)
xx = np.zeros(6)
print("xx = ", xx)
xx[1] = 1.0
print("xx = ", xx)
# what is the fft of an impulse?
yy = np.fft.fft(xx)
print("yy = fft(xx) = ", yy)  # whoops... complex numbers!
print("yy = |fft(xx)| =  ", np.abs(yy))  # so plot magnitude

# what if take the fft of yy?  fft is reversible, but "magnitude amplification" problem
xx = np.fft.fft(yy)
print("xx = fft(yy) = fft(fft(xx)) = ", np.round(np.abs(xx)))  # rounding errors; round so tiny numbers are zero

# so ifft is the fft except divides by N to prevent magnitude amplification
xx = np.fft.ifft(yy)
print("xx = ifft(yy) = ifft(fft(xx)) = ", np.round(np.abs(xx)))  # rounding errors; round so tiny numbers are zero
