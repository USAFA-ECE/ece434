% lesson3.m
% Demos for lesson 2 worksheet problem

help sampcos
% part a
sampcos(0.1,100,1000);
% part b
figure
sampcos(0.1,100,500);
% part c
figure
sampcos(0.1,100,200);
% part d
figure
sampcos(0.1,100,110);

%Aliase demonstration
%  f >= 2*Fs
%  what is the minimum Fs for 2026 Hz?


close all

%  oversampled case;   sound ok?
figure
[x, Fs] = sampcos(2, 2026, 4*2026);
sound(x,Fs);
%  critically-sampled case;   sound ok?
[x, Fs] = sampcos(2, 2026, 2*2026);
sound(x,Fs);
%  under-sampled case;   sound ok?
figure
[x, Fs] = sampcos(2, 2026, (3/2)*2026);
sound(x,Fs);
%  let f = Fs;   sound ok?  DC?
figure
[x, Fs] = sampcos(2, 2026, 2026);
sound(x,Fs);


