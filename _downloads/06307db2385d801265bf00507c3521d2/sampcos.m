function [x, fs]=sampcos(Too,fcos,fs)
% [x, fs]=sampcos(Too,fcos,[fs]) Returns a discrete-time
%     sequence of a cosine of frequency fcos in x, 
%     sampled at fs, and lasting approximately Too
%     seconds. Note Too will be adjusted to an exact
%     integer multiple of the cosine period.
%
%     Default fs is 8192 Hz.  Other common values are
%     22050 Hz and 44100 Hz.
%
%     Inputs are scalars
%     Output is a vector
%
%     If a workspace variable called doPlot equals
%     a 1 the sequence and its FFt will be plotted.
%
%     Cameron H.G. Wright, 27 Mar 97
%     Copyright (c) 1997 by Cameron H.G. Wright 

if nargin > 3
   error('Too many input arguments');
elseif nargin < 2
   error('Too few input arguments');
elseif nargin == 2
   fs=8192;  % default sampling frequency
end
cycles=round(Too*fcos);
To=cycles/fcos;
N=floor(fs*To);
dt=To/N;
df=1/To;

t=0:dt:(N-1)*dt;
f=0:df:(N-1)*df;
% the next two lines have the same effect as fftshift
fold=floor((N/2)+1); % location of the folding freq
f(fold:length(f))=f(fold:length(f))-fs;  % correct f axis

x=cos(2*pi*fcos*t);
% x=x+randn(size(x));  % a noisy version of x

% plotting section
doPlot=1;  % for debugging purposes
if doPlot == 1
   subplot(2,1,1)
   stem(t,x)
   xlabel('time (s)')
   ylabel('Sampled Cosine')
   subplot(2,1,2)
   stem(f,abs(fft(x))/N);
   xlabel('freqency (Hz)')
   ylabel('Magnitude FFT')
end

