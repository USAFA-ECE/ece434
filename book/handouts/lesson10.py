# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:18:46 2023

@author: george.york
"""
# code from lesson 10
# by George York


# import libraries
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt



from scipy.signal import blackmanharris

N = 65
w = blackmanharris(N)
plt.stem(w)

# fig 1 shows freq leak, fig2 and 3 show impact of appling hamming window
from windemo import windemo
windemo(2.5)

# does ordering of padding and windowing matter?
# does it matter if we convolve or multiply the window?
from winuse import winuse
winuse(2.5)

# example apply several windows to a signal
#windat, inline the windat.m script here
# Generation of signals for showing window effects

# WINDAT below...
# x1 from Porat p. 185
# demonstrate side-lobe masking
n1=np.arange(0,127+1)
x1=np.sin(0.3984*np.pi*n1)+(0.005*np.sin(0.5*np.pi*n1));

# x2 from Proakis/Manolakis (3rd ed) p. 435
# demonstrate main lobe smearing
# Need at least 100 actual data points to resolve all 3 freqs
n2=np.arange(0,127+1)
x2=np.cos(0.2*np.pi*n2)+np.cos(0.22*np.pi*n2)+np.cos(0.6*np.pi*n2);


# sometimes rect is the best, sometimes it is the worst
# is a dB or Linear plot the best?  depends...

from win_ana2 import win_ana2
win_ana2(x1, n1, x2, n2)

# how to zeropad in Python?
#z = np.zeros(10)
z = np.zeros(10)
print("z = ",z)
#x = np.array([1, 1, 1, 1])
x = [1, 1, 1, 1]
print("x =", x)
#x = [x z]
#x = x + list(z)
x = np.concatenate((x,z))
print("concat =",x)

# how to apply windows in Matlab?

# you can apply windows directly at the command line
#help window
# close all
plt.figure(1)
plt.plot(x1)
from scipy.signal import bartlett, hann, hamming, blackman, kaiser
x1hann = x1*(hann(128))
plt.figure(2)
plt.plot(x1hann)

# how to do a log plot?
X1hann = np.fft.fft(x1hann)
# linear plot
plt.figure(3);
plt.plot(abs(X1hann))
len(abs(X1hann))
plt.figure(4)
# log plot (only from zero to Fs/2)
plt.plot(np.arange(0,65), 20*np.log10(np.abs(X1hann[0:65])/np.max(np.abs(X1hann))))
# label frequency axis
Fs = 8000;
del_f = Fs/(64*2)
plt.figure(10)
plt.plot(np.arange(0,64*del_f,del_f), 20*np.log10(np.abs(X1hann[0:64])/np.max(np.abs(X1hann))))
#  why does the above only go 0:64 and 1:65 ?
#  why did I divide by max(abs(X1hann)) ?

# how to zeropad using FFT?
M = 1024;
X1hann = np.fft.fft(x1hann, M);
# linear plot
plt.figure(3)
plt.plot(np.abs(X1hann))
plt.figure(4);
# log plot (only from zero to Fs/2)
plt.plot(np.arange(0,int(M/2)), 20*np.log10(np.abs(X1hann[0:int(M/2)])/np.max(np.abs(X1hann))))
