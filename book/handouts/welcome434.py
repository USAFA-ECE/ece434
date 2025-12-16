# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:11:12 2020

@author: polla
"""
import scipy
print(scipy.__version__)
# import Handle song (a matlab file) into python
# get Fs (sample rate) and x (array of song samples)
from scipy.io import loadmat
song = loadmat('handel.mat')
FFFs = song['Fs']
FFs = FFFs[0]
Fs = FFs[0]
xx = song['y']
x = xx[:,0]

# Write x and Fs as a wav file, the play sound out audio port
import numpy as np
from scipy.io.wavfile import write
y = x.astype(np.float32)
write('handel.wav', Fs, y)
import winsound
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)

# what if we double Fs?
wait_for_user = input('what happens if we double Fs?')
Fs = 2*8192
write('handel.wav', Fs, y)
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)

# what if we half Fs?
wait_for_user = input('what happens if we half Fs?')
Fs = 4096
write('handel.wav', Fs, y)
winsound.PlaySound('handel.wav', winsound.SND_FILENAME)

#plot the song in the time domain in subplot
import matplotlib.pyplot as plt
plt.subplot(211)
plt.plot(x)   #plot(t,x)
#plot the frequency spectrum of the song in subplot
plt.subplot(212)
plt.psd(x,Fs=8192)
plt.show()


