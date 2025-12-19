# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 12:16:35 2025

@author: george.york
"""
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk, lfilter, remez, welch, filtfilt 

#from scipy import signal



#function upsample_demo_v3()
def upsample_demo_v3():
    # % upsample_demo()
    # %  v2 is modifyied by George York, replacing the sinusiod input signal
    # %  with a ramp input signal
    # %  v2 changes psd to pwelch
    # %
    # % Demonstrates expansion (upsampling) with interpolation
    # % by an FIR lowpass filter.
    # % The signal is a ramp, sampled at 8000 Hz.
    # % Thus the normalized frequency of the signal is 0.75pi.
    # %
    # % The signal is upsampled by a factor of 3, so the new Fs is 24 kHz,
    # % and the "new" normalized frequency is thus 0.25pi.
    # %
    # % Uses SP Toolbox routines for FIR filter design
    # % 
    # % Copyright (c) 1999,2001 Cameron H. G. Wright
    
    N=2048          # number of original samples
    #N=10
    Fs=8000			# original sample frequency
    L=3 				# upsampling factor
    N2=N*L          # new length after inserting zeros
    
    #n=0:N-1			# discrete time index vector before upsampling
    n = np.arange(0, N)
    #n2=0:N2-1		# discrete time index vector after upsampling
    n2 = np.arange(0, N2)
    
    #x=sin(2*pi*Fo*n*Ts);  % generate the sinusoidal signal
    # ramp signal
    # x(1) = 0;
    x = np.zeros(N)
    change = 1.0
    #for i=(2:N)
    for i in range(1,N):
        #x(i) = x(i-1) + change;
        x[i] = x[i-1] + change
        #if mod(i, 10)== 0:
        if i % 10 == 0:
            change = -change

    # % insert zeros into original signal
    # y=zeros(1,N2);	% create a vector of all zeros
    y = np.zeros(N2)
    # y(1:L:N2)=x;   % put samples from x properly on to y 
    y[0:N2:L] = x
    
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % pick a method to create the FIR filter coefficients appropriate for L
    # % all frequencies are normalized and expressed in pi units
    
    # % window method (hamming)
    # %b=fir2(FN,[0 PB/L 1/L 1],[1 1 0 0]);   
    
    # % window method (kaiser)
    # %[FN,Wn,beta,typ] = kaiserord([PB/L 1/L], [1 0], [dp ds]);
    # %b=fir1(FN, Wn, typ, kaiser(FN+1,8));
    # %b=fir2(FN,[0 PB/L 1/L 1],[1 1 0 0],kaiser(FN+1,8)); 
    
    # % least squares method
    # %b=firls(FN,[0 PB/L 1/L 1],[1 1 0 0]);  
    
    # % equiripple (Parks-McLelllan method)
    # [FN,fo,ao,w] = remezord( [PB/L 1/L], [1 0], [dp ds]);
    # b = remez(FN,fo,ao,w);
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    from scipy.io import loadmat
    bbb = loadmat('b.mat')
    bb = bbb['b']
    b = bb[0]
    
    # % filter the upsampled data with FIR interpolation filter
    # % filtfilt has minimal startup transients
    #yFIR=filtfilt(b,1,y);  
    # yFIR = lfilter(b, 1, y)
    yFIR = filtfilt(b, [1], y)
    a=max(abs(yFIR))
    yFIR=yFIR/a   # scale to compensate for filter gain
    
    #% set some plotting limits
    if (N > 10): 
        NP=10
    N2P=(NP*L)-(L-1)
    xmax=max(x)*1.1
    xmin=min(x)*1.1
    
    #% create plots
    plt.figure(1)
    plt.subplot(211)
    #stem(n(1:NP),x(1:NP))
    plt.stem(n[0:NP],x[0:NP])
    # axis([0 NP-1 xmin xmax])
    plt.axis([0, NP, xmin, xmax])
    plt.title('Original signal (first 10 samples)')
    plt.subplot(212)
    # stem(n2(1:N2P),y(1:N2P))
    plt.stem(n2[0:N2P],y[0:N2P])
    plt.axis([0, N2P, xmin, xmax])
    plt. title('Effect of just inserting zeros')
    plt.show()
    
    plt.figure(2)
    plt.subplot(211)
    #%psd(x,WL);
    # pwelch(x);
    # Compute the Power Spectral Density using Welch's method
    fs = 2
    f, Pxx = welch(x, fs=fs, window='hann', nperseg=256, noverlap=128, nfft=512)   
    # Plot the PSD
    plt.semilogy(f, Pxx)
    plt.title('Original PSD')
    plt.ylabel('Magnitude (dB)')
    plt.xlabel('Normalized Frequency (pi units)')
    plt.subplot(212)
    #%psd(y,WL);
    #pwelch(y);
    f, Pxx = welch(y, fs=fs, window='hann', nperseg=256, noverlap=128, nfft=512) 
    plt.semilogy(f, Pxx)
    plt.title('PSD after just inserting zeros')
    plt.ylabel('Magnitude (dB)')
    plt.xlabel('Normalized Frequency (pi units)')
    plt.show()
    
    # plt.figure(3)
    # plt.subplot(211)
    # #%psd(x,WL,Fs)
    # pwelch(x)
    # title('Original PSD')
    # ylabel('Magnitude (dB)')
    # subplot(2,1,2)
    # %psd(y,WL,Fs*L)
    # pwelch(y)
    # title('PSD after just inserting zeros')
    # ylabel('Magnitude (dB)')
    
    plt.figure(4)
    plt.subplot(2,1,1)
    #[H,F]=freqz(b,1,1024,Fs*L);
    F, H = freqz(b, 1, 1024, fs=Fs*L)
    # plot(F,20*log10(abs(H)))
    plt.plot(F, 20*np.log10(np.abs(H)))
    plt.title('Frequency response of FIR interpolator (126 order)')
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude (dB)')
    #plt.axis([0, Fs*L/2, -120, 10])
    plt.grid(True)
    plt.subplot(212)
    #%psd(yFIR,WL,Fs*L)
    # pwelch(yFIR)
    f, Pxx = welch(yFIR, fs=fs, window='hann', nperseg=256, noverlap=128, nfft=512) 
    plt.semilogy(f, Pxx)
    plt.title('PSD after inserting zeros and FIR interpolation with scaling')
    plt.ylabel('Magnitude (dB)')
    plt.show()
    
    plt.figure(5)
    plt.subplot(311)
    # stem(n(1:NP),x(1:NP))
    plt.stem(n[0:NP],x[0:NP])
    plt.axis([0, NP, xmin, xmax])
    plt.title('Original signal')
    plt.subplot(312)
    plt.stem(n2[0:N2P],y[0:N2P])
    plt.axis([0, N2P, xmin, xmax])
    plt.title('Effect of just inserting zeros')
    plt.subplot(313)
    plt.stem(n2[0:N2P],8*yFIR[0:N2P])
    plt.axis([0, N2P, xmin, xmax])
    plt.title('Effect of inserting zeros and FIR interpolation with scaling')
    plt.show()
    

    
    return
    
upsample_demo_v3()

