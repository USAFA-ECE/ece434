%  quant_t.m   function to quantize signal
% function xq = quant_t(x,b);
%	This function does quantization by truncating to the level below  
%	the signal. -1+delta/2 is the lowest level and 1-delta/2 is the highest level
%   x = input signal to be quantized
%   b = # of bits in quantizer
%  xq = quantized output signal
function xq = quant_t(x,b);

% x = x * (1-2/2^b);	% limit input to level size.
x = x - 1/2^b;	% adjust so levels are symmetric WRT 0

% limit x to range of +-1.
% x_lim = x.*(x>=-1 & x<=1) + (x<=-1 | x>=1).*sign(x); 
xq = floor(x * 2^(b-1))/(2^(b-1));

% make anything greater than highest level equal to highest level 
% and similarly for the lowest level
[I,J,V]=find(xq>=1);
xq(J)=(1-2/2^b)*ones(1,length(J));
[I,J,V]=find(xq<=-1);
xq(J)=-ones(1,length(J));
xq = xq + 1/2^b;	% adjust so levels are symmetric WRT 0