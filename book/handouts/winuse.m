function x=winuse(C)
% x=winuse(C)
%     Demonstrates use of window smoothing. Shows a discrete-time
%     sequence of a cosine of frequency 100 Hz and its 3rd harmonic, 
%     sampled at 2000 Hz, for C complete cycle(s), with it's FFT.
%     Also shows the FFT with correct and incorrect windowing.
%     Only positive half of the magnitude spectrum is plotted.
%     
%     Cameron H.G. Wright, 25 Sep 97
%     Copyright (c) 1997 by Cameron H.G. Wright

fcos=100;
fs=2000;
N=floor(fs/fcos*C);
To=N/fs;
cycles=To*fcos;
disp(sprintf('   Actual number of cycles = %g',cycles))
dt=1/fs;
df=1/To;
n=0:N-1;

M=3*N; % length after zero padding
M2=floor(M/2);
k=0:M2-1; % only half the spectrum will be plotted
nTs=0:dt:(N-1)*dt;

x=cos(2*pi*fcos*nTs) + cos(2*pi*3*fcos*nTs);
xwa=conv(x,hamming(length(x))'); % wrong method
xwap=[xwa zeros(1,(M-N))]; % pad the above sequence
xp=[x zeros(1,(M-N))];  % zero pad the original samples
xwb=xp.*hamming(length(xp))'; % another wrong method
xwc=x.*hamming(length(x))'; % correct method step1
xwcp=[xwc zeros(1,(M-N))]; % correct method step 2

% special lengths to account for convolution length
ka=0:floor(length(xwap)/2)-1;
Ma=floor(length(xwap)/2);

% take FFT of the sequences
magX=abs(fft(x));
magXP=abs(fft(xp));
magXWAP=abs(fft(xwap));
magXWB=abs(fft(xwb));
magXWCP=abs(fft(xwcp));

% plotting section
doPlot=1;  % for debugging purposes
if doPlot == 1
   figure(1)
   subplot(2,1,1)
   stem(nTs,x)
   xlabel('time (s)')
   ylabel('Sampled Signal')
   subplot(2,1,2)
   stem(n,magX);
   xlabel('k')
   ylabel('Mag FFT no zero pad')
   figure(2)
   subplot(4,1,1)
   stem(k,magXP(1:M2))
   xlabel('k')
   ylabel('padded - no win')
   subplot(4,1,2)
   stem(ka,magXWAP(1:Ma)); % length affected by convolution
   xlabel('k')
   ylabel('conv win')
   subplot(4,1,3)
   stem(k,magXWB(1:M2));
   xlabel('k')
   ylabel('pad first')
   subplot(4,1,4)
   stem(k,magXWCP(1:M2));
   xlabel('k')
   ylabel('correct')
   figure(3)
   subplot(4,1,1)
   plot(k,magXP(1:M2))
   xlabel('k')
   ylabel('padded - no win')
   subplot(4,1,2)
   plot(ka,magXWAP(1:Ma)); % length affected by convolution
   xlabel('k')
   ylabel('conv win')
   subplot(4,1,3)
   plot(k,magXWB(1:M2));
   xlabel('k')
   ylabel('pad first')
   subplot(4,1,4)
   plot(k,magXWCP(1:M2));
   xlabel('k')
   ylabel('correct')
   
   figure(1)
end

