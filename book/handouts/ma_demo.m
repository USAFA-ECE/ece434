function y = ma_demo(x,N)
% y = ma_demo(x,N)
% Computes the moving average of sequence x using a window N 

M=length(x);
if (N > M) N = M; end 
n=0:M-1;
b=(1/N)*ones(1,N);
a=[1 0];  % make sure zplane knows this is a vector
y=filter(b,1,x);
figure(1)
subplot(2,1,1)
stem(n,x);
ylabel('input x')
subplot(2,1,2)
stem(n,y);
ylabel('output y')
figure(2)
subplot(2,1,1)
plot(n,x);
ylabel('input x')
subplot(2,1,2)
plot(n,y);
ylabel('output y')
figure(3)
freqz(b,1);
figure(4)
zplane(b,a);


figure(1)

