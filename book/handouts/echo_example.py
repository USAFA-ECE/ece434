# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 08:06:43 2025

@author: george.york
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk, lfilter


#load cpx1.bin -mat

from scipy.io import loadmat
song = loadmat('cpx1.bin')
FFFs = song['Fs']
FFs = FFFs[0]
Fs = FFs[0]
xx = song['x4']
x = xx[0,:]

#sound(x4, Fs)
from scipy.io.wavfile import write
y = x.astype(np.float32)
write('dsp.wav', Fs, y)
import winsound
winsound.PlaySound('dsp.wav', winsound.SND_FILENAME)

#pause(2)
import time
# Pause for 2 seconds
time.sleep(2)

# echo delay of 1 seconds
time_delay = 1
n_delay = time_delay*Fs

#new_length = length(x4) + n_delay;
new_length = len(x) + n_delay

#x4_echo = zeros(1, new_length);
x4_echo = np.zeros(new_length, dtype=float)

#x4_zeros_after = [x4 zeros(1, n_delay)];
n_delay_zeros = np.zeros(n_delay, dtype=float)
x4_zeros_after = np.concatenate((x, n_delay_zeros))

#x4_zeros_before = [zeros(1, n_delay) x4];
x4_zeros_before = np.concatenate((n_delay_zeros, x))

#x4_echo = x4_zeros_after + x4_zeros_before;
x4_echo = x4_zeros_after + x4_zeros_before

#attenuated echo
x4_echo = x4_zeros_after + 0.5*x4_zeros_before

#sound(x4_echo, Fs)
from scipy.io.wavfile import write
y = x4_echo.astype(np.float32)
write('x4_echo.wav', Fs, y)
import winsound
winsound.PlaySound('x4_echo.wav', winsound.SND_FILENAME)

#pause(2)
import time
# Pause for 2 seconds
time.sleep(2)

# now add more echos
new_length = len(x) + n_delay + n_delay
n_delay_delay_zeros = np.zeros(2*n_delay, dtype=float)
#x4_first_term = [x4 zeros(1, n_delay) zeros(1, n_delay)];
x4_first_term = np.concatenate((x, n_delay_delay_zeros))
#x4_second_term = [zeros(1, n_delay) x4 zeros(1, n_delay)];
x4_second_term = np.concatenate((n_delay_zeros, x, n_delay_zeros))
#x4_third_term = [zeros(1, n_delay) zeros(1, n_delay) x4];
x4_third_term = np.concatenate((n_delay_delay_zeros, x))

#x4_echo = x4_first_term + 0.5*x4_second_term + 0.25*x4_third_term;
x4_echo = x4_first_term + 0.5*x4_second_term + 0.25*x4_third_term

#sound(x4_echo, Fs)
from scipy.io.wavfile import write
y = x4_echo.astype(np.float32)
write('x4_echo.wav', Fs, y)
import winsound
winsound.PlaySound('x4_echo.wav', winsound.SND_FILENAME)
