function x=freqleak(C)
% x=freqleak(C)
%     Demonstrates frequency leakage. Shows a discrete-time
%     sequence of a cosine of frequency 100 Hz, 
%     sampled at 2000 Hz, for C complete cycle(s), with it's FFT.
%     Also shows 2C sequences patched together.
%     
%     Cameron H.G. Wright, 3 Sep 97
%     Copyright (c) 1997 by Cameron H.G. Wright

fcos=100;
fs=2000;
N=floor(fs/fcos*C);
To=N/fs;
cycles=To*fcos;
disp(sprintf('   Actual number of cycles = %g',cycles))
dt=1/fs;
df=1/To;

t=0:dt:(N-1)*dt;
k=0:(N-1);


x=cos(2*pi*fcos*t);
x2=[x x];
t2=0:dt:(2*N-1)*dt;

% plotting section
doPlot=1;  % for debugging purposes
if doPlot == 1
   figure(1)
   subplot(2,1,1)
   stem(t,x)
   xlabel('time (s)')
   ylabel('Sampled Cosine')
   subplot(2,1,2)
   stem(k,abs(fft(x))/N);
   xlabel('k')
   ylabel('Magnitude FFT')
   figure(2)
   subplot(2,1,1)
   stem(t2,x2)
   xlabel('time (s)')
   ylabel('Two Cosine Sequences')
   subplot(2,1,2)
   plot(t2,x2)
   xlabel('time (s)')
   ylabel('Smoothed Version')
   figure(1)
end

