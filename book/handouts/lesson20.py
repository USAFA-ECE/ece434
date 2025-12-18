# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 09:40:42 2025

@author: george.york
"""
#
# code used for lesson 21
# by George York
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk, lfilter

# moving average demo
#help ma_demo   # uses filter command (FIR)
#load handel
# ----------------------------------------
# Simulate filtering a real signal (placeholder for 'handel')
# ----------------------------------------
from scipy.io import loadmat
song = loadmat('handel.mat')
FFFs = song['Fs']
FFs = FFFs[0]
Fs = FFs[0]
xx = song['y']
x = xx[:,0]

def zplane(b, a, title='Z-plane'):
    z, p, k = tf2zpk(b, a)
    plt.figure()
    ax = plt.subplot(111)
    # Draw unit circle
    uc = plt.Circle((0, 0), radius=1, fill=False, color='black', linestyle='dashed')
    ax.add_patch(uc)
    # Plot zeros and poles
    plt.plot(np.real(z), np.imag(z), 'go', label='Zeros')
    plt.plot(np.real(p), np.imag(p), 'rx', label='Poles')
    plt.title(title)
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

#function y = ma_demo(x,N)
def ma_demo(x, N):
    # moving average demo
    # y = ma_demo(x,N)
    # Computes the moving average of sequence x using a window N 
    M=len(x)
    if (N > M):
        N = M
    n= np.arange(0,M) # not M-1
    b=(1/N)*np.ones(N, dtype=float)
    a=np.array([1.0, 0.0]) # make sure zplane knows this is a vector
    #y=filter(b,1,x);
    y = lfilter(b, 1, x)
    plt.figure(1)
    plt.subplot(211)
    plt.stem(n,x)
    plt.ylabel('input x')
    plt.subplot(212)
    plt.stem(n,y)
    plt.ylabel('output y')
    plt.show()
    plt.figure(2)
    plt.subplot(211)
    plt.plot(n,x)
    plt.ylabel('input x')
    plt.subplot(212)
    plt.plot(n,y);
    plt.ylabel('output y')
    plt.show()
    plt.figure(3)
    #plt.freqz(b,1);
    w, h = freqz(b, 1)
    plt.figure(4)
    plt.plot(w, 20 * np.log10(abs(h)))
    plt.title('Frequency Response (mov average)')
    plt.xlabel('Frequency [rad/sample]')
    plt.ylabel('Magnitude [dB]')
    plt.grid(True)
    plt.show()
    plt.figure(5)
    #zplane(b,a);
    zplane(b, a, title='Z-plane (moving avg example)')
    #figure(1)
    return(y)

y2 = ma_demo(x, 200)

#sound(100*y2,Fs)
from scipy.io.wavfile import write
yy = y2.astype(np.float32)
write('handel.wav', Fs, 100*yy)
import winsound
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)


#annual return demo: 
#   invest $250 per month at 1# compounded monthly for 240 months
# n = 0:239
# h = 250*(1.01).^n
# figure(5)
# stem(n,h)
# s1 = 240*250
# s2 = sum(h)

# another way
# del y
# y(1) = 0;
N = 241
y = np.zeros(N, dtype=float)
#y_bad(1) = 0;
y_bad = np.zeros(N, dtype=float)
#for (n= 2:241):
for n in range(1, N): # not N-1
    y[n] = 1.01*y[n-1]+250;
    y_bad[n] = y_bad[n-1] + 250;

y_finalanswer = y[240]
y_bad_finalanswer = y_bad[240]
plt.figure(6)
plt.stem(y, 'b')
#hold on
plt.stem(y_bad, 'r')
plt.show()