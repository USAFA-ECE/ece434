# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:29:51 2023

@author: george.york
"""

# % [x, fs]=sampcos(Too,fcos,[fs]) Returns a discrete-time
# %     sequence of a cosine of frequency fcos in x, 
# %     sampled at fs, and lasting approximately Too
# %     seconds. Note Too will be adjusted to an exact
# %     integer multiple of the cosine period.
# %
# %     Default fs is 8192 Hz.  Other common values are
# %     22050 Hz and 44100 Hz.
# %
# %     Inputs are scalars
# %     Output is a vector
# %
# %     If a workspace variable called doPlot equals
# %     a 1 the sequence and its FFt will be plotted.
# %
# import libraries
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def sampcos(Too=None, fcos=None, Fs=None):
    """ Too is the time duration of the sampled sine wave
        fcos is the frequency of the sine wave
        Fs is cthe sample rate
    """
    # Too = 0.1
    # fcos = 100
    # Fs = 1000
    cycles = round(Too * fcos)
    To = float(cycles / fcos)
    N  = int(Fs * To)  # naturally truncates
    dt = To / N
    df = 1 / To
    t = np.arange(0,(N)*dt,dt)  # not N-1
    f = np.arange(0,(N)*df,df) 
    f_shifted = f - df * (N/2)  # also shift axis for plot
    pi = sp.pi
    x=np.cos(2*pi*fcos*t)
    
    # plot section
    plt.subplot(211)
    plt.stem(t, x)   #plt.stem(t,x)
    plt.xlabel('time (s)')
    plt.ylabel('Sampled Cosine')
    #plot the frequency spectrum of the song in subplot
    plt.subplot(212)
    plt.stem(f_shifted, np.abs(np.fft.fftshift(np.fft.fft(x)))/N)
    plt.xlabel('freqency (Hz)')
    plt.ylabel('Magnitude FFT')
    plt.show()
    
    
    return [x, Fs]
