function lesson2()
% by George York
% copyright (c) 2004 George York

% looking at Discrete Data
load handel
% how do you see the variables loaded?
whos
% Fs is the sample frequency
% y is the data

% How do you see the 1st 10 values?
%pickme(1)
y(1:10)
% How do you what these numbers mean?  not in voltage land anymore
% How do you plot?
plot(y(1:10))
% this looks analog... use stem for instead for discrete data
stem(y(1:10))
% How do I determine the sample frequency?
Fs
% Fs = 8192 
% How can I hear this data?
sound(y, Fs)
% what if?
sound(y, Fs*2)
% what if?
sound(y, Fs/2)
% wasn't that easy to manipulate digitally?  how would you build an analog
% circuit to do that?  or a mechanical system?

% How can we see the frequency of the data?
plot(abs(fft(y)))
plot(fftshift(abs(fft(y))))
plot(-Fs/2:(Fs/length(y)):(Fs/2-(Fs/length(y))), fftshift(abs(fft(y))))
% we will learn other ways later

% Lets LPF the data, using sptool [deprecated], so use fdatool
% create an LPF, fc=600 Hz
%sptool
fdatool
% or load filt1.mat
load filt1.mat
% how can I find out how to use the filter command?
help filter
y2= filter(filt1.tf.num, 1, y);

% plot the LPF data
hold on
plot(-Fs/2:(Fs/length(y2)):(Fs/2-(Fs/length(y2))), fftshift(abs(fft(y2))))
% Look Mom! No Capacitors required!
% can you hear the difference?
sound(y2, Fs)
sound(y, Fs)