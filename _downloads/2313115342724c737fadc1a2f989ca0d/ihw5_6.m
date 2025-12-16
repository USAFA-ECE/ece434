function ihw5_6()
% Ingle/Proakis HW Problem P5.6: 
% Compares DTFT to DFT for a sequence.
%
% Copyright 1998 Cameron H. G. Wright 
%
x = [1,2,3,4,5,6,6,5,4,3,2,1]; % data sequence x[n] 
% optional variation to play "whatif?"
% x = [0:0.5:6.5, 6:-0.5:0.5]; % modifed data sequence x[n] 
% x=[x, zeros(1,25)];  % zero padding of data sequence x[n]
n = 0:length(x)-1;
figure(1)
stem(n,x)
title('Discrete-Time Data Sequence'); 
xlabel('Sample'); 
ylabel('Magnitude')
% DFT analysis
kd=n;
Xd=fft(x);
magXd = abs(Xd); angXd = angle(Xd);
figure(2);
% plot with negative frequency swapped to the left half
% use normalized pi units for discrete radian frequency axis
wn= (kd-floor(length(kd)/2))/floor(length(kd)/2);
subplot(2,1,1); stem(wn,fftshift(magXd)); grid on;
title('DFT Magnitude'); 
xlabel('frequency in pi units'); 
ylabel('Magnitude')
subplot(2,1,2); stem(wn,fftshift(angXd)); grid on;
title('DFT Phase'); 
xlabel('frequency in pi units'); 
ylabel('Radians')

% DTFT analysis
kf = -500:500; w = (pi/500)*kf;  % [-pi, pi] axis divided into 1001 points.
Xf = x * (exp(-j*pi/500)) .^ (n'*kf); % DTFT using matrix-vector product
magXf = abs(Xf); angXf = angle(Xf);
figure(3)
subplot(2,1,1); plot(w/pi,magXf); grid
title('DTFT Magnitude'); 
xlabel('frequency in pi units'); 
ylabel('Magnitude')
subplot(2,1,2); plot(w/pi,angXf); grid
title('DTFT Angle'); 
xlabel('frequency in pi units'); 
ylabel('Radians')

% Superimpose the two plots
% Note the x-axis range must be the same for both
figure(4);
subplot(2,1,1); stem(wn,fftshift(magXd),'r');
hold on; plot(w/pi,magXf); 
title('DFT and DTFT Magnitude'); 
xlabel('frequency in pi units'); 
ylabel('Magnitude')
hold off;
subplot(2,1,2); stem(wn,fftshift(angXd),'r'); 
hold on; plot(w/pi,angXf);
title('DFT and DTFT Angle'); 
xlabel('frequency in pi units'); 
ylabel('Radians')
hold off;

figure(1)


