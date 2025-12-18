% ee434 lesson 18 class demo code
%   by George York

% For HW 4.11, find the poles and zeros
b = [1 -1.619 1]  
a = [1 -1.516 0.878]
[z, p, k] = tf2zp(b, a)
% plot the Zplane
help zplane
figure(1)
zplane(b, a)
% freqz:  transfer functions
help freqz
figure(2)
freqz(b, a)


% For other example in class
b = [1]  
a = [1 0 0.81]
figure(3)
zplane(b,a)
figure(4)
freqz(b, a)
