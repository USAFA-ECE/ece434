% demo of linear, cicular, and FFT convolution
%  by George York
%
x = [1 -3 7]
h = [4 2 -6]
% linear convolution
y_linear = conv(x,h)
% circular convolution
y_circular = real(ifft(fft(x).*fft(h)))
% zero pad to make FFT approach linear
L = length(x) + length(h) - 1
y_linear_fft = real(ifft(fft(x,L).*fft(h,L)))

% using convolution to LPF a song
%
% open song file
load handel;
x = y;
% simple LPF coefficients
h = [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1];
y = conv(x,h);
%original
soundsc(x, Fs)
%after LPF
soundsc(y, Fs)

figure(1)
L = length(x) + length(h) - 1
plot(abs(fft(h,L)))
figure(2)
plot(abs(fft(x,L)))
figure(3)
plot(abs(fft(y,L)))
