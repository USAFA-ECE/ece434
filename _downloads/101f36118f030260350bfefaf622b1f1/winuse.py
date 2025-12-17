# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:18:46 2023

@author: george.york
"""


# import libraries
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def winuse(C=None):

    # x=winuse(C)
    #     Demonstrates use of window smoothing. Shows a discrete-time
    #     sequence of a cosine of frequency 100 Hz and its 3rd harmonic, 
    #     sampled at 2000 Hz, for C complete cycle(s), with it's FFT.
    #     Also shows the FFT with correct and incorrect windowing.
    #     Only positive half of the magnitude spectrum is plotted.
    #     
    # by George York

    fcos=100
    fs=2000
    N=np.floor(fs/fcos*C)
    To=N/fs
    cycles=To*fcos
    print('   Actual number of cycles = ',cycles)
    dt=1/fs
    df=1/To
    #n=0:(N-1)
    n = np.arange(0,N)
    
    M=3*N  # length after zero padding
    M2= np.floor(M/2);
    #k=0:M2-1; % only half the spectrum will be plotted
    k = np.arange(0,M2)
    #nTs=0:dt:(N-1)*dt;
    nTs = np.arange(0,N*dt,dt)
    
    x=np.cos(2*np.pi*fcos*nTs) + np.cos(2*np.pi*3*fcos*nTs);
 
    from scipy.signal import hamming
    xwa=np.convolve(x,hamming(len(x))) # wrong method
    xwap=np.concatenate((xwa, np.zeros(int(M-N)))) # pad the above sequence
    xp=np.concatenate((x, np.zeros(int(M-N))))  # zero pad the original samples
    xwb=xp*hamming(len(xp)) # another wrong method
    xwc=x*hamming(len(x)) # correct method step1
    xwcp=np.concatenate((xwc, np.zeros(int(M-N)))) # correct method step 2
    
    # special lengths to account for convolution length
    ka=np.arange(0,np.floor(len(xwap)/2))
    Ma=np.floor(len(xwap)/2)
    
    # take FFT of the sequences
    magX=np.abs(np.fft.fft(x));
    magXP=np.abs(np.fft.fft(xp));
    magXWAP=np.abs(np.fft.fft(xwap));
    magXWB=np.abs(np.fft.fft(xwb));
    magXWCP=np.abs(np.fft.fft(xwcp));
    
    # plotting section


    plt.figure(1)
    plt.subplot(211)
    plt.stem(nTs,x)
    plt.xlabel('time (s)')
    plt.ylabel('Sampled Signal')
    plt.subplot(212)
    plt.stem(nTs,magX);
    plt.xlabel('k')
    plt.ylabel('Mag FFT no zero pad')
    plt.show()
    plt.figure(2)
    plt.subplot(411)
    plt.stem(k,magXP[0:int(M2)])
    plt.xlabel('k')
    plt.ylabel('padded - no win')
    plt.subplot(412)
    plt.stem(ka,magXWAP[0:int(Ma)]) # length affected by convolution
    plt.xlabel('k')
    plt.ylabel('conv win')
    plt.subplot(413)
    plt.stem(k,magXWB[0:int(M2)])
    plt.xlabel('k')
    plt.ylabel('pad first')
    plt.subplot(414)
    plt.stem(k,magXWCP[0:int(M2)]);
    plt.xlabel('k')
    plt.ylabel('correct')
    plt.show()
    plt.figure(3)
    plt.subplot(411)
    plt.plot(k,magXP[0:int(M2)])
    plt.xlabel('k')
    plt.ylabel('padded - no win')
    plt.subplot(412)
    plt.plot(ka,magXWAP[0:int(Ma)]) # length affected by convolution
    plt.xlabel('k')
    plt.ylabel('conv win')
    plt.subplot(413)
    plt.plot(k,magXWB[0:int(M2)])
    plt.xlabel('k')
    plt.ylabel('pad first')
    plt.subplot(414)
    plt.plot(k,magXWCP[0:int(M2)])
    plt.xlabel('k')
    plt.ylabel('correct')


    return [x]
