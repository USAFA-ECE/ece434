% ee434 lesson 17 class demo code
%   by George York

% example running a difference equation (low pass filter)
x = [0 3 1 2 7 3]
y = [0 0 0 0 0 0]
for n=2:6
    y(n) = 0.5*x(n) + 0.5*y(n-1)
end
figure(1)
plot(x, 'r')
hold on
plot(y, 'g')

% demo matlab's zplane and other Z functions... poles and zeros etc
% freqz:  transfer functions
help freqz
b = [0.5]  
a = [1 -0.5]
figure(2)
freqz(b, a)
% what if move pole to 0.9?
figure(3)
a = [1 -0.9]
b = [0.4]
freqz(b, a)

% plot the Zplane
help zplane
figure(3)
zplane(b, a)

% lets filter a real signal
load handel
x=y;
sound(x,Fs)
for n=2:length(y)
    y(n) = 0.4*x(n) + 0.9*y(n-1);
end
sound(y,Fs)


% look at FFT before/after LPF  
figure(4)
plot(abs(fft(x)), 'r')
hold on
plot(abs(fft(y)), 'g')
% log scale
figure(5)
z = abs(fft(x));
plot(20*log10(z/max(z)), 'r')
hold on
z = abs(fft(y));
plot(20*log10(z/max(z)), 'g')

%make into an HPF?
a = [1 +0.9]

figure(6)
zplane(b,a)

figure(7)
freqz(b,a)
for n=2:length(y)
    y(n) = 0.4*x(n) - 0.9*y(n-1);
end
sound(y,Fs)
figure(4)
hold on
plot(abs(fft(y)), 'b')

figure(5)
hold on
z = abs(fft(y));
plot(20*log10(z/max(z)), 'b')





