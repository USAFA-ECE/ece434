% This script shows a method to find the gain of H(z) during Bilinear
% Transformation

a1 = [-0.9925 + 0.0264*i, -0.9925 - 0.0264*i];
a2 = a1(1)+a1(2);
a3 = a1(1)*a1(2);
num = [1 0 -1];
den = [1 a2 a3];
freqz(num, den)
H = freqz(num, den);
peak = max(abs(H))
K = 1/peak

num = K*[1 0 -1];
den = [1 a2 a3];
freqz(num, den)