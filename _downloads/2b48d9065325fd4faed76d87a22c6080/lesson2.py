# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:11:12 2020

@author: polla
"""
 
#change to work directory
#cd "C:\Users\polla\.spyder-py3\python_matlab"

# import libraries
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# import Handle song (a matlab file) into python
# get Fs (sample rate) and x (array of song samples)
from scipy.io import loadmat
song = loadmat('handel.mat')
FFFs = song['Fs']
FFs = FFFs[0]
Fs = FFs[0]
xx = song['y']
x = xx[:,0]

# how to see the variables
#whos

# how do you see the 1st 10 samples?
x[0:10]
print(x[0:10])

# how to plot first 10 samples
plt.plot(x[0:10])   #plot(t,x)
plt.show()

# how to do a stem plot for discreet data
plt.stem(x[0:10])   
plt.show()

# Write x and Fs as a wav file, the play sound out audio port
from scipy.io.wavfile import write
y = x.astype(np.float32)
write('handel.wav', Fs, y)
import winsound
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)

# what if we double Fs?
wait_for_user = input('what happens if we double Fs?')
write('handel.wav', 2*Fs, y)
import winsound
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)

# what if we half Fs?
wait_for_user = input('what happens if we half Fs?')
write('handel.wav', 4096, y)
import winsound
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)

#plot the song in the time domain in subplot
plt.subplot(211)
plt.plot(x)   #plot(t,x)
#plot the frequency spectrum of the song in subplot
plt.subplot(212)
plt.psd(x,Fs=8192)
plt.show()


# filter command. scipy.signal.lfitler
from scipy import signal
# make LPF with Fc = 400 H
Fc = 400 / (Fs / 2)
b, a = signal.butter(9, Fc, 'lowpass', 'ba')
y = signal.lfilter(b, a, x)
gain = max(x)/max(y)
y = gain * y
#plot the frequency spectrum of the original and filtered song in subplot
plt.figure(2)
plt.psd(x,Fs=8192)
plt.psd(y,Fs=8192)
plt.show()
# listen to LPF version
yy = y.astype(np.float32)
write('handel.wav', Fs, yy)
import winsound
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)


#example of creating and plotting a sinusoid
plt.figure(3)
pi = sp.pi
t = np.arange(0,4,0.001)
plt.plot(t,np.cos(2*pi*t))
plt.show()

