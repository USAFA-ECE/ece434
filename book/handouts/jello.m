function y=jello
[y, Fs]=audioread('operational.wav');
Ts=1/Fs;
n=0:length(y)-1;
z=0.9*cos(2*pi*1000*n*Ts);
r=y'+z;
