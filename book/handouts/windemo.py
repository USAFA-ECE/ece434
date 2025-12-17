# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:18:46 2023

@author: george.york
"""


# import libraries
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def windemo(C=None):

    # x=windemo(C)
    #     Demonstrates window smoothing. Shows a discrete-time
    #     sequence of a cosine of frequency 100 Hz, 
    #     sampled at 2000 Hz, for C complete cycle(s), with it's FFT.
    #     Also shows 2C sequences patched together, with it's FFT.
    #     Then shows 2C sequences smoothed with hamming, with it's FFT.
    #     
    # by George York

    fcos=100
    fs=2000
    N=np.floor(fs/fcos*C)
    To=N/fs
    cycles=To*fcos
    print('   Actual number of cycles = ', cycles)
    dt=1/fs
    df=1/To
    
    #t=0:dt:(N-1)*dt
    t = np.arange(0,(N)*dt,dt)
    #n=0:(N-1)
    n = np.arange(0,N)
    
    x=np.cos(2*np.pi*fcos*t)
    #x2=[x x];
    x2 = np.concatenate((x, x))
    #t2=0:dt:(2*N-1)*dt;
    t2 = np.arange(0,(2*N)*dt,dt)
    
    # plotting section
    plt.figure(1)
    plt.subplot(211)
    plt.stem(t,x)
    plt.xlabel('time (s)')
    plt.ylabel('Sampled Cosine')
    plt.subplot(212)
    X=np.abs(np.fft.fft(x))/N;
    plt.stem(n,X);
    plt.xlabel('k')
    plt.ylabel('Magnitude FFT')
    plt.figure(2)
    plt.subplot(211)
    plt.stem(t2,x2)
    plt.xlabel('time (s)')
    plt.ylabel('Two Cosine Sequences')
    plt.subplot(212)
    from scipy.signal import hamming
    xw=x*hamming(len(x));
    #x2w=[xw xw];    
    x2w = np.concatenate((xw, xw))
    plt.stem(t2,x2w);
    plt.xlabel('time (s)')
    plt.ylabel('Windowed Sequences')
    plt.figure(3)
    plt.subplot(211)
    plt.stem(n,X);
    plt.xlabel('k')
    plt.ylabel('Mag FFT no win')
    plt.subplot(212)
    XW=np.abs(np.fft.fft(xw))/N;
    plt.stem(n,XW);
    plt.xlabel('k')
    plt.ylabel('Mag FFT with win') 
    
    return [x]
