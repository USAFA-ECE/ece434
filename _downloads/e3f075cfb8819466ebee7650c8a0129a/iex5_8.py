# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:18:46 2023

@author: george.york
"""
# function iex5_8()
# % Ingle/Proakis Chap 5: Example 5.8: HiDen vs. HiRes Spectrum

# import libraries
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


# generate the full signal
n = np.arange(0,100) # not N-1
pi = sp.pi
x=np.cos(0.48*pi*n) + np.cos(0.52*pi*n)

# Spectrum based on the first 10 samples of x(n)
n1 = np.arange(0,10)
y1 = x[0:10:1]
plt.figure(1)
plt.subplot(211)
plt.stem(n1,y1)
plt.title('signal x(n), 0 <= n <= 9')
plt.xlabel('n')
plt.axis([0,10,-2.5,2.5])
Y1=np.fft.fft(y1)
magY1=np.abs(Y1[0:6])
k1= np.arange(0,6)
w1=2*pi/10*k1
plt.subplot(212)
plt.stem(w1/pi,magY1)
plt.title('Samples of DFT Magnitude')
plt.xlabel('frequency in pi units')
plt.axis([0,1,0,10])

n2 = np.arange(0,50)
y2 = np.concatenate((x[0:10:1], np.zeros(40)))
plt.figure(2)
plt.subplot(211)
plt.stem(n2,y2);
plt.title('signal x(n), 0 <= n <= 9 + 40 zeros')
plt.xlabel('n')
plt.axis([0,50,-2.5,2.5])
Y2=np.fft.fft(y2);
magY2=np.abs(Y2[0:26])
k2= np.arange(0,26)
w2=2*pi/50*k2
plt.subplot(212)
plt.stem(w2/pi,magY2)
plt.title('DFT Magnitude')
plt.xlabel('frequency in pi units')
plt.axis([0,1,0,10])


# High density spectrum (100 samples) based on the first 10 samples of x(n)
n3 = np.arange(0,100)
y3 = np.concatenate((x[0:10:1], np.zeros(90)))
plt.figure(3)
plt.subplot(211)
plt.stem(n3,y3)
plt.title('signal x(n), 0 <= n <= 9 + 90 zeros')
plt.xlabel('n')
plt.axis([0,100,-2.5,2.5])
Y3=np.fft.fft(y3);
magY3=np.abs(Y3[0:51])
k3= np.arange(0,51)
w3=2*pi/100*k3
plt.subplot(212)
plt.stem(w3/pi,magY3)
plt.title('DFT Magnitude')
plt.xlabel('frequency in pi units')
plt.axis([0,1,0,10])


# High density spectrum (500 samples) based on the first 10 samples of x(n)
n4 = np.arange(0,500)
y4 = np.concatenate((x[0:10:1], np.zeros(490)))
plt.figure(4)
plt.subplot(2,1,1)
plt.stem(n4,y4)
plt.title('signal x(n), 0 <= n <= 9 + 490 zeros')
plt.xlabel('n')
plt.axis([0,500,-2.5,2.5])
Y4=np.fft.fft(y4);
magY4=np.abs(Y4[0:251])
k4= np.arange(0,251)
w4=2*pi/500*k4
plt.subplot(212)
plt.stem(w4/pi,magY4)
plt.title('DFT Magnitude')
plt.xlabel('frequency in pi units')
plt.axis([0,1,0,10])

# High resolution spectrum based on 100 samples of the signal x(n)
plt.figure(5)
plt.subplot(211)
plt.stem(n,x)
plt.title('signal x(n), 0 <= n <= 99')
plt.xlabel('n')
plt.axis([0,100,-2.5,2.5])
X=np.fft.fft(x);
magX=np.abs(X[0:51])
k= np.arange(0,51)
w=2*pi/100*k
plt.subplot(212)
plt.stem(w/pi,magX)
plt.title('DFT Magnitude')
plt.xlabel('frequency in pi units')
plt.axis([0,1,0,60])