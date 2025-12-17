function x=windemo(C,win)
% x=windemo(C)
%     Demonstrates window smoothing. Shows a discrete-time
%     sequence of a cosine of frequency 100 Hz, 
%     sampled at 2000 Hz, for C complete cycle(s), with it's FFT.
%     Also shows 2C sequences patched together, with it's FFT.
%     Then shows 2C sequences smoothed with hamming, with it's FFT.
%     
%     Cameron H.G. Wright, 15 Sep 97
%     Copyright (c) 1997 by Cameron H.G. Wright
%     Modified by Maj C. Hendrix, 2 Sep 2011

fcos=100;
fs=2000;
N=floor(fs/fcos*C);
To=N/fs;
cycles=To*fcos;
disp(sprintf('   Actual number of cycles = %g',cycles))
dt=1/fs;
df=1/To;

t=0:dt:(N-1)*dt;
n=0:(N-1);

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
   X=abs(fft(x))/N;
   stem(n,X);
   xlabel('k')
   ylabel('Magnitude FFT')
   
   figure(2)  
   subplot(3,1,1)
   stem(t2,x2)
   xlabel('time (s)')
   ylabel('Two Cosine Sequences')
   subplot(3,1,2)
   xh=hamming(length(x))';
   x2h=[xh xh];
   stem(t2,x2h);
   xlabel('time (s)')
   ylabel('Hamming Window')
   subplot(3,1,3)
   xw=x.*hamming(length(x))';
   x2w=[xw xw];
   stem(t2,x2w);
   xlabel('time (s)')
   ylabel('Windowed Sequences')
   
   figure(3)
   subplot(2,1,1)
   stem(n,X);
   xlabel('k')
   ylabel('Mag FFT no win')
   subplot(2,1,2)
   XW=abs(fft(xw))/N;
   stem(n,XW);
   xlabel('k')
   ylabel('Mag FFT with win')

   figure(1)
end

