# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 14:20:37 2025

@author: george.york
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk, lfilter

def phasedemo(terms=None, offset=None):
    
    """ Demonstrates the effect of nonlinear phase
    % response by phase shifting Fourier terms of 
    % a square wave defined by 
    %
    % y(t) = 4/pi[sin wt + (1/3)sin 3wt +...]
    %
    % Usage: phasedemo(terms,offset)
    %
    % where "terms" are the number of
    % Fourier series terms and where
    % "offset" is a boolean (0 or 1) that
    % determines if the the phase is corrupted
    % by up to +/- pi/2 radians
    """
    
    # if nargin==0 
    #    terms=21;
    #    offset=0; 
    # end
    # if nargin==1 
    #    offset=0; 
    # end
    
    #n_terms_string=num2str(terms);
    n_terms_string=str(terms)
    
    #n=1:2:terms;  % odd harmonics
    #n = np.arange(1, terms, 2)
    n = np.arange(1, terms + 1, 2).reshape(-1, 1)    
    
    #n=n'; % make n a column vector
    f=100  # fundamental frequency
    T=1/f  # period
    #t=0:T/400:2*T;  % time axis is a row vector
    #t = np.arange(0,2*T,T/400)
    t = np.arange(0, 2 * T + T / 400, T / 400)  # time axis as row vector
    if offset!=0:
       scaling=np.pi/2
       # rn1=rand(size(t))*scaling;
       rn1=np.random.rand(t.size)*scaling
       # rn2=rand(size(t))*scaling;
       rn2=np.random.rand(t.size)*scaling
       rn=rn2-rn1 # gives -pi/2 < rn < pi/2
    else:
       #rn=zeros(size(t));
       rn = np.zeros(t.size)

    #x=n*t; % create matrix
    # Reshape n to a column vector and t to a row vector
    # n_col = n.reshape(-1, 1)  # shape (3, 1)
    # t_row = t.reshape(1, -1)  # shape (1, 3)
    # # Matrix multiplication
    # x = n_col @ t_row
    x = n @ t.reshape(1, -1)  # create matrix
    x=2*np.pi*f*x
    for i in range(len(n)):
       for j in range(len(t)):
          #x(i,j)=(4/pi)/n(i)*sin(x(i,j)-rn(j));
          #x[i-1,j-1]= (4/np.pi)/n[i-1]*np.sin(x[i-1,j-1]-rn[j-1])
          x[i, j] = (4 / np.pi) / n[i, 0] * np.sin(x[i, j] - rn[j])

    #y=sum(x);
    y = np.sum(x, axis=0)
    if terms<=2:
       y=np.sin(2*np.pi*f*t);

    
    plt.figure(1)
    plt.plot(t,y)
    plt.axis([0, 2*T, -1.5, 1.5])
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(f'{n_terms_string}-Term Fourier Series for a Square Wave')
    plt.show()
        
    return 
