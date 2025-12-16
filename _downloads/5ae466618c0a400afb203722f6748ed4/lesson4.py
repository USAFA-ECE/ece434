# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:08:36 2023

@author: george.york
"""

# Lesson4: demo effects of quantization error (both rounding and truncating)

# load wav file
# import libraries
import scipy as sp
from scipy.io import wavfile
from scipy.io.wavfile import write
import winsound
import numpy as np

wait_for_user = input('This is the original recording, 8-bits per sample')
# hit enter key to continue
winsound.PlaySound('operational.wav', winsound.SND_FILENAME)
Fs, y = wavfile.read('operational.wav')
Ts = 1 / Fs
# create an output array
x = np.zeros(len(y), np.uint8)

wait_for_user = input('hear what happens when we quantize to 6 bits (rounding)')

# max_y = max(y)   this is 255
# min_y = min(y)   this is 0
# avg_y = np.mean(y) this is 130.7
# looks like samples are uint8

for i in range(0, len(y)):
    if (y[i] & 0b00000011) > 0b00000010: # greater than 1/2 way, so round up
        if (y[i] & 0b00000011) == 0b11111100:  # but if already max, don't roll over
            x[i] = y[i] & 0b11111100
        else: # round up
            x[i] = (y[i] & 0b11111100) + 0b00000100
    else: 
        x[i] = y[i] & 0b11111100
write('operational6r.wav', Fs, x)
winsound.PlaySound('operational6r.wav', winsound.SND_FILENAME)

wait_for_user = input('hear what happens when we quantize to 6 bits (truncating)')
x = y & 0b11111100
write('operational6t.wav', Fs, x)
winsound.PlaySound('operational6t.wav', winsound.SND_FILENAME)


wait_for_user = input('hear what happens when we quantize to 3 bits (rounding)')

for i in range(0, len(y)):
    if (y[i] & 0b00011111) > 0b00010000:  # greater than 1/2 way, so round up
        if (y[i] & 0b00011111) == 0b11100000:  # but if already max, don't roll over
            x[i] = y[i] & 0b11100000
        else:
            x[i] = (y[i] & 0b11100000) + 0b00100000
    else:   # less than 1/2 way so round down
        x[i] = y[i] & 0b11100000
write('operational3r.wav', Fs, x)
winsound.PlaySound('operational3r.wav', winsound.SND_FILENAME)

wait_for_user = input('hear what happens when we quantize to 3 bits (truncating)')
x = y & 0b11100000
write('operational3t.wav', Fs, x)
winsound.PlaySound('operational3t.wav', winsound.SND_FILENAME)