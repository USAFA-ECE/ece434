% code used for lesson 21
% by George York

% moving average demo
help ma_demo   % uses filter command (FIR)
load handel
y2 = ma_demo(y, 200);
sound(100*y2,Fs)

%annual return demo: 
%   invest $250 per month at 1% compounded monthly for 240 months
% n = 0:239
% h = 250*(1.01).^n
% figure(5)
% stem(n,h)
% s1 = 240*250
% s2 = sum(h)

% another way
clear y
y(1) = 0;
y_bad(1) = 0;
for (n= 2:241)
    y(n) = 1.01*y(n-1)+250;
    y_bad(n) = y_bad(n-1) + 250;
end
y(241)
y_bad(241)
figure(6)
stem(y, 'b')
hold on
stem(y_bad, 'r')

