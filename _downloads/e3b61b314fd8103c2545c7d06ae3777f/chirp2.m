function x = chirp2(N)
% x = chirp2(N); 
%     returns x, a two channel discrete-time
%     sequence containing a chirp signal, sweeping frequencies
%     for 1 Hz to 8000 Hz (the sample frequency), over and over
%     up to N (the number of samples).
%
%     To hear
%         x = chirp2(N);
%         soundsc(x,8000);
%     To see spectogram (may have to zoom in)
%         specgram(x(:,1),256,8000,256, 250);
%
%     Letting N = 8000 is one second.
%
%     George W.P. York, 29 Jul 03
%     Copyright (c) 2003 by George W.P. York
%
Fs = 8000;       % sample frequency
n=1:.2:N;
f=1:.2:N;

left = cos(2*pi.*n.*f/Fs);
right = left;
x(:,1) = left(:);
x(:,2) = right(:);




 

