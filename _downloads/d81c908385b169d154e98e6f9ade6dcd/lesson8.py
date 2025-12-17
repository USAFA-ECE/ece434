# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:16:58 2023

@author: george.york
"""

# % demo of linear, cicular, and FFT convolution
# %  by George York
# %
# import libraries
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, -3, 7])
N = len(x)
Fs = 10
T = 1/Fs
#n = 0:1:(N-1);
n = np.arange(0,N) 
#k = 0:1:(N-1);
k = np.arange(0,N) 
#t = 0:T:((N-1)*T)
#t = np.arange(0,(N)*T,T) 
t = np.arange(0,0.3,T) #hard codeing N*T
del_f = Fs/N
#f = 0:del_f:((N-1)*del_f)
f = np.arange(0,(N)*del_f,del_f)
plt.stem(n, x)
plt.show()
h = np.array([4, 2, -6])
# linear convolution
y_linear = np.convolve(x,h)
print("y_linear = ", y_linear)

# 1st try at FFT Based Convolution
y_1st = np.abs((np.fft.ifft(np.fft.fft(x)*np.fft.fft(h))))
print("y_1st =", y_1st)

# circular convolution
y_circular = np.abs((np.fft.ifft(np.fft.fft(x)*np.fft.fft(h))))

# zero pad to make FFT approach linear
L = len(x) + len(h) - 1
y_linear_fft = np.abs((np.fft.ifft(np.fft.fft(x,L)*np.fft.fft(h,L))))
print("y_linear_fft =", y_linear_fft)

# using convolution to LPF a song
#
# open song file
from scipy.io import loadmat
song = loadmat('handel.mat')
FFFs = song['Fs']
FFs = FFFs[0]
Fs = FFs[0]
#x = song['y']
x = song['y'].flatten()

# simple LPF coefficients
#h = [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1];
h = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

y = np.convolve(x,h)

#original
# soundsc(x, Fs)
# Write x and Fs as a wav file, the play sound out audio port
from scipy.io.wavfile import write
xx = x.astype(np.float32)
write('handel.wav', Fs, xx)
import winsound
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)

#after LPF
# soundsc(y, Fs)
yy = y.astype(np.float32)
write('handel.wav', Fs, yy)
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)


plt.figure(1)
L = len(x) + len(h) - 1
plt.plot(np.abs(np.fft.fft(h,L)))
plt.show()
plt.figure(2)
plt.plot(np.abs(np.fft.fft(x,L)))
plt.show()
plt.figure(3)
plt.plot(np.abs(np.fft.fft(y,L)))
plt.show()

