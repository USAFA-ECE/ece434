# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 14:37:59 2025

@author: george.york
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, lfilter, tf2zpk

# ee434 lesson 18 class demo code
#   by George York

# For HW 4.11, find the poles and zeros
b = [1, -1.619, 1]  
a = [1, -1.516, 0.878]
z, p, k = tf2zpk(b, a)
# plot the Zplane
#help zplane
# ----------------------------------------
# Z-plane plot with unit circle
# ----------------------------------------
def zplane(b, a, title='Z-plane'):
    z, p, k = tf2zpk(b, a)
    plt.figure()
    ax = plt.subplot(1, 1, 1)
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

zplane(b, a, title='Z-plane (HW 4.11)')

# freqz:  transfer functions
#help freqz
w, h = freqz(b, a)

plt.figure(2)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Frequency Response (HW 4.11)')
plt.xlabel('Frequency [rad/sample]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()

a = [1, -0.9]
b = [0.4]
w, h = freqz(b, a)
plt.figure(3)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Frequency Response ()')
plt.xlabel('Frequency [rad/sample]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()

# For other example in class
b = [1]  
a = [1, 0, 0.81]
plt.figure(4)
zplane(b,a, title='Z-plane ()')

w, h = freqz(b, a)
plt.figure(5)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Frequency Response ()')
plt.xlabel('Frequency [rad/sample]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()

# For other example in class [lesson 19]
b = [1, -.9]   
a = [1, 0, 0.81]
plt.figure(6)
zplane(b,a, title='Z-plane ()')

w, h = freqz(b, a)
plt.figure(7)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Frequency Response ()')
plt.xlabel('Frequency [rad/sample]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()