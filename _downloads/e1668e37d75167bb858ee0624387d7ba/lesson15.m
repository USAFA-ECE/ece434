% example plotting transfer function in Z-plane
% 1st define numerator and denominator of transfer function
num = [1 -2.4 2.88];
den = [1 -0.8 0.64];
% find poles and zeros
[z, p, k] = tf2zp(num, den)
% plot in Z-plane
figure(1)
zplane(num, den)
% see frequency response
figure(2)
freqz(num, den)
