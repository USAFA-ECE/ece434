function phasedemo(terms,offset)
% 
% Demonstrates the effect of nonlinear phase
% response by phase shifting Fourier terms of 
% a square wave defined by 
%
% y(t) = 4/pi[sin wt + (1/3)sin 3wt +...]
%
% Usage: phasedemo(terms,offset)
%
% where "terms" are the number of
% Fourier series terms and where
% "offset" is a boolean (0 or 1) that
% determines if the the phase is corrupted
% by up to +/- pi/2 radians
%
% Copyright (c) 2000 Cameron H. G. Wright
%

if nargin==0 
   terms=21;
   offset=0; 
end
if nargin==1 
   offset=0; 
end
n_terms_string=num2str(terms);

n=1:2:terms;  % odd harmonics
n=n'; % make n a column vector
f=100;  % fundamental frequency
T=1/f; % period
t=0:T/400:2*T;  % time axis is a row vector
if offset~=0
   scaling=pi/2;
   rn1=rand(size(t))*scaling;
   rn2=rand(size(t))*scaling;
   rn=rn2-rn1; % gives -pi/2 < rn < pi/2
else
   rn=zeros(size(t));
end
x=n*t; % create matrix
x=2*pi*f*x;
for i=1:length(n),
   for j=1:length(t),
      x(i,j)=(4/pi)/n(i)*sin(x(i,j)-rn(j));
   end
end
y=sum(x);
if terms<=2
   y=sin(2*pi*f*t);
end

figure(1)
plot(t,y);
axis([0 2*T -1.5 1.5])
xlabel('Time')
ylabel('Amplitude')
title([n_terms_string,'-Term Fourier Series for a Square Wave'])


