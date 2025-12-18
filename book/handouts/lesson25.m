% example using REMEZ for multipass filter
mag = [0.5 0.0 1.0 1.0 0.5 0.5]
fpts = [0 0.2 0.4 0.6 0.8 1.0]
h = remez(30, fpts, mag);
length(h)
[H,w]= freqz(h,1,100);
figure(1)
plot(abs(H))

%now let's try to filter a signal with this filter design impulse reponse h
%Create a random noise input signal x[n]
x = randn(70000,1);
X = fft(x);
%linear plot the input signals frequency response before filtering
figure(2)
subplot(2,1,1)
plot((abs(X)/max(abs(X))));
ylabel('White Noise Input')
% now filter the signal with this multiband LPF filter h, and plot linear
y = filter(h, 1, x);
Y = fft(y);
subplot(2,1,2)
plot((abs(Y)/max(abs(Y))));
ylabel('Filtered White Noise')

% Flaky example using REMEZ for multipass filter
mag = [0.5 0.0 1.0 1.0 0.5 0.5]
fpts = [0 0.2 0.4 0.6 0.8 1.0]
h = remez(32, fpts, mag);
[H,w]= freqz(h,1,100);
figure(3)
plot(abs(H))


% try class example (hann = 50 order; equirripple = 18 order)
mag = [1 1 0 0]
fpts = [0 .25 .375 1]
h = remez(30, fpts, mag);
[H,w]= freqz(h,1,100);
plot(abs(H))
length(h)
% log plot
figure(4)
plot(20*log10(abs(H)/max(abs(H))));

% try to reduce order to equirripple
mag = [1 1 0 0];
fpts = [0 .25 .375 1];
h = remez(18, fpts, mag);
[H,w]= freqz(h,1,100);
length(h)
% log plot
figure(5)
plot(20*log10(abs(H)/max(abs(H))));

% try again; order 22 works
mag = [1 1 0 0];
fpts = [0 .25 .375 1];
h = remez(22, fpts, mag);
[H,w]= freqz(h,1,100);
length(h)
% log plot
figure(6)
plot(20*log10(abs(H)/max(abs(H))));

%now let's try to filter a signal with this filter design impulse reponse h
%Create a random noise input signal x[n]
x = randn(70000,1);
X = fft(x);
%log plot the input signals frequency response before filtering
figure(7)
subplot(2,1,1)
plot(20*log10(abs(X)/max(abs(X))));
ylabel('White Noise Input')
% now filter the signal with this multiband LPF filter h, and log plot
y = filter(h, 1, x);
Y = fft(y);
subplot(2,1,2)
plot(20*log10(abs(Y)/max(abs(Y))));
ylabel('Filtered White Noise')

