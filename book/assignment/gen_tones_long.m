function x = gen_tones_long(N)
% x = gen_tones_long(N); 
%     returns x, a two channel discrete-time
%     sequence containing various tones for testing 
%     the voice removal application
%     N is the number of samples sampled at Fs=48000 Hz.
%     So letting N=48000 will be one second of sound
%
%     To hear
%         x = gen_tones_long(N);
%         soundsc(x,48000);
%
%     George W.P. York, 29 Jul 03
%     Copyright (c) 2003 by George W.P. York
%
fs = 48000;       % sample frequency
% N  = 48000;       % number of samples
T  =  1/fs;       % time between samples
n=1:N;     % 

% create test tones as sampled sinusoids
left  = (cos(2*pi*105*n*T) + cos(2*pi*126*n*T) + cos(2*pi*151*n*T) + cos(2*pi*175*n*T) + cos(2*pi*225*n*T) + cos(2*pi*301*n*T) + cos(2*pi*401*n*T)                     + cos(2*pi*601*n*T)  + cos(2*pi*1001*n*T) + cos(2*pi*1501*n*T)                      + cos(2*pi*8001*n*T) + cos(2*pi*10001*n*T));
right = (cos(2*pi*105*n*T) + cos(2*pi*126*n*T) + cos(2*pi*151*n*T) + cos(2*pi*175*n*T) + cos(2*pi*225*n*T)                     + cos(2*pi*401*n*T) + cos(2*pi*501*n*T) + cos(2*pi*601*n*T)                       + cos(2*pi*1501*n*T) + cos(2*pi*2001*n*T)                      + cos(2*pi*10001*n*T) + cos(2*pi*12001*n*T));
x(:,1) = left(:);
x(:,2) = right(:);

% plotting section
% n2=1:(N/2);
% n3=0:((N/2)-1);
% figure(1)
% subplot(2,1,1);
% leftplot = abs(fft(x(:,1))).*(2/N);
% stem(n3,leftplot(n2));
% xlabel('frequency (Hz)')
% ylabel('Left Channel')
% subplot(2,1,2);
% rightplot = abs(fft(x(:,2))).*(2/N);
% stem(n3,rightplot(n2));
% xlabel('frequency (Hz)')
% ylabel('Right Channel')


 

