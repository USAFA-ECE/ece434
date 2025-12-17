# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:23:49 2023

@author: george.york
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:29:51 2023

@author: george.york
"""

# function x=freqleak(C)
# % x=freqleak(C)
# %     Demonstrates frequency leakage. Shows a discrete-time
# %     sequence of a cosine of frequency 100 Hz, 
# %     sampled at 2000 Hz, for C complete cycle(s), with it's FFT.
# %     Also shows 2C sequences patched together.
# %
# import libraries
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# from freqleak import freqleak

def freqleak(C=None):
    #C = 2.5
    fcos=100
    fs=2000
    N=np.floor(fs/fcos*C)
    To=N/fs
    cycles=To*fcos
    print("   Actual number of cycles = ", cycles)
    dt=1/fs
    df=1/To
    
    t = np.arange(0,(N)*dt,dt)  # not N-1
    k = np.arange(0,(N)*1,1) 
    
    pi = sp.pi
    x=np.cos(2*pi*fcos*t)    

    x2= np.concatenate((x, x))
    t2 = np.arange(0,(2*N)*dt,dt)  # not N-1

    
    # plotting section

    plt.figure(1)
    plt.subplot(211)
    plt.stem(t,x)
    plt.xlabel('time (s)')
    plt.ylabel('Sampled Cosine')
    plt.subplot(212)
    plt.stem(k,np.abs(np.fft.fft(x))/N)
    plt.xlabel('k')
    plt.ylabel('Magnitude FFT')
    plt.figure(2)
    plt.subplot(211)
    plt.stem(t2,x2)
    plt.xlabel('time (s)')
    plt.ylabel('Two Cosine Sequences')
    plt.subplot(212)
    plt.plot(t2,x2)
    plt.xlabel('time (s)')
    plt.ylabel('Smoothed Version')

    return [x]
