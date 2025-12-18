# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 07:43:34 2025

@author: george.york
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk, lfilter, remez

# MATLAB vs Python remez Differences
# In MATLAB:

# You provide a list of frequency points and corresponding magnitudes directly.

# In Python (scipy.signal.remez):

# You must define frequency bands as pairs (start, stop).
# The desired list must match the number of bands (i.e., half the length of fpts).
# You also need to specify weights for each band.
# THe default assumption is that the sampling frequency is 1.0, so the Nyquist frequency is 0.5. Therefore, all band edges must be strictly less than 0.5 

# Define frequency bands as pairs: [start1, stop1, start2, stop2, ...]
# Scale bands to fit within [0, 0.5]
# bands = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]


# # Desired gains for each band
# desired = [0.0, 1.0, 0.5]

# # Equal weight for each band
# weights = [1, 1, 1]

# # Design the filter with 30 taps
# h = remez(30, bands, desired, weight=weights)

# set fs=2 for normalized
h = remez(
    numtaps=31,
    bands=[0, 0.2, 0.4, 0.6, 0.8, 1.0],
    desired=[0.0, 1.0, 0.5],
    weight=[1, 1, 1],
    fs=2
)

# Output the length of the filter
print(len(h))

#w, h = freqz(h, 1)
#w, h = freqz(h, 1, 100)
#w, h = freqz(h, worN=512, fs=2)
w, H = freqz(h, 1, fs=2)
plt.figure(1)
plt.plot(abs(H))
plt.title('Frequency Response (multiband)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

# now let's try to filter a signal with this filter design impulse reponse h
#Create a random noise input signal x[n]
#x = randn(70000,1);
x = np.random.randn(70000, 1)
x = x.flatten()
#X = fft(x);
X = np.fft.fft(x)

#linear plot the input signals frequency response before filtering
plt.figure(2)
plt.subplot(211)
plt.plot((abs(X)/max(abs(X))));
plt.ylabel('White Noise Input')

# now filter the signal with this multiband LPF filter h, and plot linear
# y = filter(h, 1, x);
y = lfilter(h, 1, x)
#y = np.convolve(x,h)
Y = np.fft.fft(y)
plt.subplot(212)
plt.plot((abs(Y)/max(abs(Y))))
plt.ylabel('Filtered White Noise')
plt.show()


# try class example (hann = 50 order; equirripple = 18 order)
# mag = [1 1 0 0]
# fpts = [0 .25 .375 1]
# h = remez(30, fpts, mag);
# set fs=2 for normalized
h = remez(
    numtaps=31,
    bands=[0, 0.25, 0.375, 1.0],
    desired=[1.0, 0.0],
    weight=[1, 1],
    fs=2
)
#[H,w]= freqz(h,1,100);
w, H = freqz(h, 1, fs=2)
plt.figure(3)
plt.plot(abs(H))
plt.title('Frequency Response (multiband)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()
 
#plt.plot(abs(H))
#length(h)
# Output the length of the filter
print(len(h))

# % log plot
# figure(4)
# plot(20*log10(abs(H)/max(abs(H))));
plt.figure(4)
plt.plot(20*np.log10(abs(H)/max(abs(H))))
plt.title('Frequency Response (multiband)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()


# try to reduce order to equirripple
# mag = [1 1 0 0];
# fpts = [0 .25 .375 1];
# h = remez(18, fpts, mag);
h = remez(
    numtaps=19,
    bands=[0, 0.25, 0.375, 1.0],
    desired=[1.0, 0.0],
    weight=[1, 1],
    fs=2
)

# [H,w]= freqz(h,1,100);
# length(h)
print(len(h))
w, H = freqz(h, 1, fs=2)

# log plot
# figure(5)
# plot(20*log10(abs(H)/max(abs(H))));
plt.figure(5)
plt.plot(20*np.log10(abs(H)/max(abs(H))))
plt.title('Frequency Response (multiband)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()

# % try again; order 22 works
# mag = [1 1 0 0];
# fpts = [0 .25 .375 1];
# h = remez(22, fpts, mag);
h = remez(
    numtaps=23,
    bands=[0, 0.25, 0.375, 1.0],
    desired=[1.0, 0.0],
    weight=[1, 1],
    fs=2
)

# [H,w]= freqz(h,1,100);
# length(h)
print(len(h))
w, H = freqz(h, 1, fs=2)

# % log plot
# figure(6)
# plot(20*log10(abs(H)/max(abs(H))));
plt.figure(6)
plt.plot(20*np.log10(abs(H)/max(abs(H))))
plt.title('Frequency Response (multiband)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude [dB]')
plt.grid(True)
plt.show()

# %now let's try to filter a signal with this filter design impulse reponse h
# %Create a random noise input signal x[n]
# x = randn(70000,1);
x = np.random.randn(70000, 1)
x = x.flatten()
#X = fft(x);
X = np.fft.fft(x)

#log plot the input signals frequency response before filtering
# figure(7)
# subplot(2,1,1)
# plot(20*log10(abs(X)/max(abs(X))));
# ylabel('White Noise Input')
plt.figure(7)
plt.subplot(211)
plt.plot(20*np.log10(abs(X)/max(abs(X))))
plt.ylabel('White Noise Input')

# % now filter the signal with this multiband LPF filter h, and log plot
# y = filter(h, 1, x);
y = lfilter(h, 1, x)
#y = np.convolve(x,h)
Y = np.fft.fft(y)
plt.subplot(212)
plt.plot(20*np.log10(abs(Y)/max(abs(Y))))
plt.ylabel('Filtered White Noise')
plt.show()




