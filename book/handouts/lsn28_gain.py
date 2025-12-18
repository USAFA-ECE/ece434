# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 13:13:09 2025

@author: george.york
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk, lfilter, remez
from scipy import signal

# This script shows a method to find the gain of H(z) during Bilinear Transformation

a1 = np.array([-0.9925 + 0.0264j, -0.9925 - 0.0264j])
#a2 = a1(1)+a1(2);
a2 = a1[0]+a1[1]
#a3 = a1(1)*a1(2);
a3 = a1[0]*a1[1]
num = np.array([1., 0., -1.])
den = np.array([1., a2, a3])
#H = freqz(num, den);
w, H = freqz(num, den, fs=2)
plt.figure(1)
plt.plot(abs(H))
plt.title('Frequency Response')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

z, p, k = signal.tf2zpk(num, den)
print("Zeros:", z)
print("Poles:", p)
print("Gain:", k)





peak = max(abs(H))
print(peak)
K = 1/peak

num = K*num;
#den = [1 a2 a3];
#freqz(num, den)
w, H = freqz(num, den, fs=2)
plt.figure(2)
plt.plot(abs(H))
plt.title('Frequency Response [normalized]')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

z, p, k = signal.tf2zpk(num, den)
print("Zeros:", z)
print("Poles:", p)
print("Gain:", k)

# Plot in Z-plane
# zplane(num, den)
plt.figure(3)
plt.title("Z-plane Plot")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.grid()

# Plot unit circle
theta = np.linspace(0, 2 * np.pi, 1000)
unit_circle = np.exp(1j * theta)
plt.plot(np.real(unit_circle), np.imag(unit_circle), 'k--', label='Unit Circle')

# Plot zeros and poles
plt.scatter(np.real(z), np.imag(z), marker='o', label='Zeros')
plt.scatter(np.real(p), np.imag(p), marker='x', label='Poles')
plt.legend()
plt.axis('equal')
plt.show()