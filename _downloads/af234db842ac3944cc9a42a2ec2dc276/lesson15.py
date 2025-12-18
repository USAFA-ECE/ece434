# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 15:21:16 2025

@author: george.york
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define numerator and denominator of the transfer function
num = [1, -2.4, 2.88]
den = [1, -0.8, 0.64]

# Find zeros, poles, and gain
z, p, k = signal.tf2zpk(num, den)
print("Zeros:", z)
print("Poles:", p)
print("Gain:", k)

# Plot in Z-plane
plt.figure(1)
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

# Frequency response
w, h = signal.freqz(num, den)
plt.figure(2)
plt.title("Frequency Response")
plt.plot(w / np.pi, 20 * np.log10(abs(h)))
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Magnitude (dB)")
plt.grid()
plt.show()
