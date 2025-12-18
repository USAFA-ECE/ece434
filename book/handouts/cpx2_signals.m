load cx2.bin -mat
whos
figure(1)
fx1 = abs(fft(x1));
plot(20*log10(fx1/max(fx1)), 'r')

figure(2)
fx2 = abs(fft(x2));
plot(20*log10(fx2/max(fx2)), 'r')


figure(3)
plot(x4a);

load noisy
whos

figure(4)
fx2 = abs(fft(x2));
plot(20*log10(fx2/max(fx2)), 'r')
sound(x2,Fx)

figure(5)
fy1 = abs(fft(y1));
plot(20*log10(fy1/max(fy1)), 'r')
sound(y1,Fy)
