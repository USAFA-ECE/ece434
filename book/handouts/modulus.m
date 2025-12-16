% Example using modulus math to find aliased frequency
% CPH1, part b:
Fs = 1500
Aliased250 = mod((250+Fs/2),Fs)-Fs/2
Aliased450 = mod((450+Fs/2),Fs)-Fs/2
Aliased1000 = mod((1000+Fs/2),Fs)-Fs/2
Aliased2750 = mod((2750+Fs/2),Fs)-Fs/2
Aliased4050 = mod((4050+Fs/2),Fs)-Fs/2
