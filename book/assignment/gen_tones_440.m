function gen_tones_440

%
fs = 48000;       % sample frequency
N  = 10*48000;       % number of samples
T  =  1/fs;       % time between samples
n=1:N;     % 

% create test tones as sampled sinusoids
left  = 100*(cos(2*pi*440*n*T));
right = 100*(cos(2*pi*440*n*T));
x(:,1) = left(:);
x(:,2) = right(:);

% plotting section
n2=1:(N/16);
n3=0:((N/16)-1);
figure(1)
subplot(2,1,1);
plot(right(1:400));
xlabel('time')
ylabel('Right Channel')
subplot(2,1,2);
rightplot = abs(fft(x(:,2))).*(2/N);
stem(n3,rightplot(n2));
xlabel('frequency (Hz)')
ylabel('Right Channel')

sound(x,fs)
