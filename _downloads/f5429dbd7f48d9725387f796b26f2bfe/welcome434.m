function welcome434()
% by George York

% looking at Discrete Data
load handel

% How can I hear this data?
sound(y, Fs)
R = input('next?');
% what if?
sound(y, Fs*2)
R = input('next?');
% what if?
sound(y, Fs/2)
% wasn't that easy to manipulate digitally?  how would you build an analog
% circuit to do that?  or a mechanical system?
figure(2)
% How can we see the frequency of the data?
plot(-Fs/2:(Fs/length(y)):(Fs/2-(Fs/length(y))), fftshift(abs(fft(y))))