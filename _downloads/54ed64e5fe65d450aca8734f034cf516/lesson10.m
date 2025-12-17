% lesson 10

% matlab has several window function built-in
help window

N  = 65;
w  = window(@blackmanharris,N);
stem(w)

help windemo
% fig 1 shows freq leak, fig2 and 3 show impact of appling hamming window
windemo(2.5);

help winuse
% does ordering of padding and windowing matter?
% does it matter if we convolve or multiply the window?
winuse(2.5);

% example apply several windows to a signal
windat
help win_ana2
% sometimes rect is the best, sometimes it is the worst
% is a dB or Linear plot the best?  depends...
win_ana2

% how to zeropad in Matlab?
help zeros
z = zeros(1, 10)
x = [1 1 1 1]
x = [x z]

% how to apply windows in Matlab?


% you can apply windows directly at the command line
help window
close all
plot(x1)
x1hann = x1.*transpose(window(@hann,128));
figure(2);
plot(x1hann)

% how to do a log plot?
X1hann = fft(x1hann);
% linear plot
figure(3);
plot(abs(X1hann))
length(abs(X1hann))
figure(4);
% log plot (only from zero to Fs/2)
plot(0:64, 20*log10(abs(X1hann(1:65))/max(abs(X1hann))));

% label frequency axis
Fs = 8000;
del_f = Fs/(64*2);
figure(10);
plot(0:del_f:64*del_f, 20*log10(abs(X1hann(1:65))/max(abs(X1hann))));
%  why does the above only go 0:64 and 1:65 ?
%  why did I divide by max(abs(X1hann)) ?

% how to zeropad using FFT?
M = 1024;
X1hann = fft(x1hann, M);
% linear plot
figure(3);
plot(abs(X1hann))
figure(4);
% log plot (only from zero to Fs/2)
plot(0:M/2, 20*log10(abs(X1hann(1:(M/2)+1))/max(abs(X1hann))));

% how to apply windows in Matlab?
% another way is to use wintool
wintool
