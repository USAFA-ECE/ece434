# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 12:50:53 2023

@author: george.york
"""
import matplotlib.pyplot as plt
import numpy as np

# function DFT_demo(fo, Fs, N)
# % example use:  DFT_demo(100,800,8)
# % demos an N-point DFT of a fo Hz sinusoid sampled at Fs Hz. 
# % Pauses between each calculation.
fo = 100
Fs = 800
N = 8

nn = np.arange(0,N,1)  # goes from 0 to N-1, incrementing by 1
#i = np.arange(1,N+1,1)  # goes from 1 to N, incrementing by 1
x = np.cos(2*np.pi*(fo/Fs)*nn)
DFT_bins = np.zeros(N)

plt.figure(1)
plt.subplot(411)
plt.stem(nn,x)
plt.xlabel('n')
plt.ylabel('x[n]')


# now manually walk through DFT
for k in range(0, N):
    print("k = ", k)
    real_mult = np.zeros(N)
    imag_mult = np.zeros(N)
    k_sum = 0 + 0j
    for n in range(0, N):
        print("   n = ", n)
        W = np.exp(-1j*2*np.pi*k*n/N)
        print("   W = ", W)
        # plt.subplot(422)
        #compass(W)
        # r = np.abs(W)
        # #theta = np.degrees(W)
        # theta = np.angle(W)
        # # theta = cmath.phase(w)
        # fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        # ax.plot(theta, r)
        # plt.xlabel('phasor W')
        plt.subplot(412)
        value = x[n]*W
        print("   x[n] = ", x[n])
        print("   x[n]*W = ", value)
        #real_mult[n+1]=real(x(n+1)*W);
        real_mult[n] = value.real
        plt.stem(nn,real_mult, 'r')
        plt.xlabel('n')
        plt.ylabel('Real(x[n]*W)')
        #%subplot(4,2,4)
        #%compass(real(W))
        plt.subplot(413)
        #imag_mult(n+1)=imag(x(n+1)*W)
        imag_mult[n]=value.imag
        plt.stem(nn,imag_mult, 'r')
        plt.xlabel('n')
        plt.ylabel('Imag(x[n]*W)')
        #%subplot(4,2,6)
        #%compass(imag(W))
        k_sum = k_sum + value;
        
        #pause
        # also show other data
        plt.subplot(411)
        plt.stem(nn,x)
        plt.xlabel('n')
        plt.ylabel('x[n]')
        plt.subplot(414)
        plt.stem(nn,DFT_bins);
        plt.xlabel('k')
        plt.ylabel('DFT')
        
        plt.show()
        input_value = input('Next data x (hit return)?\n')
    plt.subplot(414)
    DFT_bins[k]= np.abs(k_sum);
    plt.stem(nn,DFT_bins);
    plt.xlabel('k')
    plt.ylabel('DFT')
    #pause
    plt.show()
    input_value = input('Next bin k (hit return)?\n')
