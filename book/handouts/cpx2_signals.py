# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 15:33:31 2025

@author: george.york
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt



#load cpx2.bin -mat
from scipy.io import loadmat
data = loadmat('cpx2.bin')
x1 = data['x1'].flatten()
FFs = data['Fs'].flatten()
Fs = FFs[0]

plt.figure(1)
plt.plot(x1)

N = len(x1)
del_f = Fs / N

plt.figure(2)
fx2 = np.abs(np.fft.fft(x1))

#f = 0:del_f:((N-1)*del_f)
f = np.arange(0,(N)*del_f,del_f)
plt.plot(f, 20*np.log10(fx2/np.max(fx2)), 'r')


# sound(x1, Fs)
# Write x and Fs as a wav file, the play sound out audio port
from scipy.io.wavfile import write
xx = x1.astype(np.float32)
write('cpx2_x1.wav', Fs, xx)
import winsound
winsound.PlaySound('cpx2_x1.wav', winsound.SND_FILENAME)


#load cpx2_x8.bin -mat
data_x8 = loadmat('cpx2_x8.bin')
x8 = data_x8['x8'].flatten()
FFs_x8 = data_x8['Fs_x8'].flatten()
Fs_x8 = FFs_x8[0]

plt.figure(1)
plt.plot(x8)
plt.figure(2)
fx8 = np.abs(np.fft.fft(x8))
N = len(x8)
del_f8 = Fs_x8 / 8

#f = 0:del_f8:(N-1)*del_f8
f = np.arange(0,(N)*del_f8,del_f8)
plt.plot(f, 20*np.log10(fx8/np.max(fx8)), 'r')

#sound(x8, Fs_x8)
xx8 = x8.astype(np.float32)
write('cpx2_x8.wav', Fs_x8, xx8)
winsound.PlaySound('cpx2_x8.wav', winsound.SND_FILENAME)

x3 = data['x3'].flatten()
FFs = data['Fs'].flatten()
plt.figure(3)
plt.plot(x3);


#load noisy
noisy = loadmat('noisy.mat')
x2 = noisy['x2'].flatten()
FFx = noisy['Fx'].flatten()
Fx = FFx[0]

plt.figure(4)
fx2 = np.abs(np.fft.fft(x2))
N = len(fx2)
del_f = Fx/N

f = np.arange(0,(N)*del_f,del_f)
plt.plot(f,20*np.log10(fx2/np.max(fx2)), 'r')

#sound(x2,Fx)
xx2 = x2.astype(np.float32)
write('cpx2_x2.wav', Fx, xx2)
winsound.PlaySound('cpx2_x2.wav', winsound.SND_FILENAME)

