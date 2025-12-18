# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 15:28:19 2025

@author: george.york
"""

# ee434 lesson 17 class demo code
#   by George York
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, lfilter, tf2zpk

# ----------------------------------------
# Simulate a low-pass filter on a short signal
# ----------------------------------------
x = np.array([0, 3, 1, 2, 7, 3])
y = np.zeros_like(x, dtype=float)

# Difference equation: y[n] = 0.5*x[n] + 0.5*y[n-1]
for n in range(1, len(x)):
    y[n] = 0.5 * x[n] + 0.5 * y[n - 1]

plt.figure(1)
plt.plot(x, 'ro-', label='Input x[n]')
plt.plot(y, 'go-', label='Output y[n]')
plt.title('Low-pass Filter Output')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

# ----------------------------------------
# Frequency response of a simple filter
# ----------------------------------------
b = [0.5]
a = [1, -0.5]
w, h = freqz(b, a)

plt.figure(2)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Frequency Response (Pole at 0.5)')
plt.xlabel('Frequency [rad/sample]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()

# ----------------------------------------
# Frequency response with pole at 0.9
# ----------------------------------------
a = [1, -0.9]
b = [0.4]
w, h = freqz(b, a)

plt.figure(3)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Frequency Response (Pole at 0.9)')
plt.xlabel('Frequency [rad/sample]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()

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

plt.figure(4)
zplane(b, a, title='Z-plane (Pole at 0.9)')

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
# Fs = 44100  # Sampling frequency
# t = np.linspace(0, 1, Fs)
# x = np.sin(2 * np.pi * 440 * t)  # 440 Hz sine wave
# y = np.zeros_like(x)

from scipy.io.wavfile import write
yy = x.astype(np.float32)
write('handel.wav', Fs, yy)
import winsound
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)


# Apply low-pass filter: y[n] = 0.4*x[n] + 0.9*y[n-1]
yyy = np.zeros_like(x, dtype=float)
for n in range(1, len(x)):
    yyy[n] = 0.4 * x[n] + 0.9 * yyy[n - 1]

from scipy.io.wavfile import write
yy = yyy.astype(np.float32)
write('handel.wav', Fs, yy)
import winsound
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)

# ----------------------------------------
# FFT before and after filtering
# ----------------------------------------
plt.figure(5)
plt.plot(np.abs(np.fft.fft(x)), 'r', label='Original')
plt.plot(np.abs(np.fft.fft(yyy)), 'g', label='Filtered (LPF)')
plt.title('FFT Before and After LPF')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(6)
z = np.abs(np.fft.fft(x))
plt.plot(20 * np.log10(z / np.max(z)), 'r', label='Original')
z = np.abs(np.fft.fft(yyy))
plt.plot(20 * np.log10(z / np.max(z)), 'g', label='Filtered (LPF)')
plt.title('Log FFT Before and After LPF')
plt.legend()
plt.grid(True)
plt.show()

# ----------------------------------------
# High-pass filter: change sign of feedback coefficient
# ----------------------------------------
a = [1, 0.9]
zplane(b, a, title='Z-plane (HPF)')

w, h = freqz(b, a)
plt.figure(7)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Frequency Response (HPF)')
plt.xlabel('Frequency [rad/sample]')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()

# Apply high-pass filter: y[n] = 0.4*x[n] - 0.9*y[n-1]
yyyy = np.zeros(len(x), dtype=float)
for n in range(1, len(x)):
    yyyy[n] = 0.4 * x[n] - 0.9 * yyyy[n - 1]

from scipy.io.wavfile import write
yy = yyyy.astype(np.float32)
write('handel.wav', Fs, yy)
import winsound
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)

plt.figure(8)
plt.plot(np.abs(np.fft.fft(x)), 'r', label='original')
plt.plot(np.abs(np.fft.fft(yyyy)), 'g', label='Filtered (HPF)')
plt.legend()
plt.show()

plt.figure(9)
z = np.abs(np.fft.fft(x))
plt.plot(20 * np.log10(z / np.max(z)), 'r', label='original')
z = np.abs(np.fft.fft(yyyy))
plt.plot(20 * np.log10(z / np.max(z)), 'b', label='Filtered (HPF)')
plt.legend()
plt.show()
