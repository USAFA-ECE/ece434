function lesson6()
% demo on DFT for lesson6 of EE434
[x, fs]=sampcos(0.005,200,4000);
y = fft(x);
figure(2);
stem(0:19,abs(y));
