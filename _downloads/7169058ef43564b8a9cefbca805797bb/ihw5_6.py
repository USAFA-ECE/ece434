# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 15:22:26 2023

@author: george.york
"""
import matplotlib.pyplot as plt
import numpy as np
# Ingle/Proakis HW Problem P5.6: 
# Compares DTFT to DFT for a sequence.

# make a data sequence, a triangle
x = np.zeros(12)
value = 1.
for i in range(0, 6):
    x[i] = value
    value = value + 1
value = 6
for i in range(6, 12):
    x[i] = value
    value = value - 1

n = np.arange(0,len(x),1)  # goes from 0 to N-1, incrementing by 1

# plot the data
plt.figure(1)
plt.stem(n,x)
plt.title('Discrete-Time Data Sequence'); 
plt.xlabel('Sample'); 
plt.ylabel('Magnitude')   

# DFT analysis
kd = n
Xd = np.fft.fft(x)
magXd = np.abs(Xd)
angXd = np.angle(Xd)
# plot with negative frequency swapped to the left half
# use normalized pi units for discrete radian frequency axis 
plt.figure(2)

N = len(x)
wn = (n - 1 * (N/2)) / (N/2)  # shift axis for plot, and scale to range to pi (+/- 1)
plt.subplot(211)
plt.stem(wn, np.fft.fftshift(magXd))
plt.grid()
plt.title('DFT Magnitude'); 
plt.xlabel('frequency in pi units'); 
plt.ylabel('Magnitude')
plt.subplot(212)
plt.stem(wn, np.fft.fftshift(angXd))
plt.grid()
plt.title('DFT Phase'); 
plt.xlabel('frequency in pi units'); 
plt.ylabel('Radians')

# DTFT Analysis
# kf = np.arange(-500,501,1)  # [-pi, pi] axis divided into 1001 points.
# w = (np.pi/500)*kf;  
# kf_conj_transpose = np.matrix(kf)
# Xf = np.power(x * (np.exp(-1.j*np.pi/500)), (n*kf_conj_transpose.getH())) # DTFT using matrix-vector product
# Instead, use DFT with many samples to appear as if it is the DTFT (continious)

N2 = 600
n2 = np.arange(0,N2,1)  # goes from 0 to N-1, incrementing by 1
kd2 = n2
# zero pad out to 600 samples to fool FFT
Xd2 = np.fft.fft(x, N2)
magXd2 = np.abs(Xd2)
angXd2 = np.angle(Xd2)

plt.figure(3)

wn2 = (n2 - 1 * (N2/2)) / (N2/2)  # shift axis for plot, and scale to range to pi (+/- 1)
plt.subplot(211)
plt.plot(wn2, np.fft.fftshift(magXd2))
plt.grid()
plt.title('DTFT Magnitude'); 
plt.xlabel('frequency in pi units'); 
plt.ylabel('Magnitude')
plt.subplot(212)
plt.plot(wn2, np.fft.fftshift(angXd2))
plt.grid()
plt.title('DTFT Phase'); 
plt.xlabel('frequency in pi units'); 
plt.ylabel('Radians')

# Superimpose the two plots
# Note the x-axis range must be the same for both
plt.figure(4)
plt.subplot(211)    
plt.stem(wn, np.fft.fftshift(magXd), 'r')
#plt.hold(True)  
plt.plot(wn2, np.fft.fftshift(magXd2))
plt.title('DFT and DTFT Magnitude'); 
plt.xlabel('frequency in pi units'); 
plt.ylabel('Magnitude')

#plt.hold(False)
plt.subplot(212)  
plt.stem(wn, np.fft.fftshift(angXd), 'r')
#plt.hold(True)   
plt.plot(wn2, np.fft.fftshift(angXd2))
plt.title('DFT and DTFT Angle'); 
plt.xlabel('frequency in pi units'); 
plt.ylabel('Radians')
#plt.hold(False)
plt.show()


