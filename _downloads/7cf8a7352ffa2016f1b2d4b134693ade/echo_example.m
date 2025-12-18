function echo_example()
% by George York
load cpx1.bin -mat
sound(x4, Fs)
pause(2)
% echo delay of 1 seconds
time_delay = 1;

n_delay = time_delay*Fs;

new_length = length(x4) + n_delay;
x4_echo = zeros(1, new_length);

x4_zeros_after = [x4 zeros(1, n_delay)];
x4_zeros_before = [zeros(1, n_delay) x4];

x4_echo = x4_zeros_after + x4_zeros_before;

%attenuated echo
x4_echo = x4_zeros_after + 0.5*x4_zeros_before;

sound(x4_echo, Fs)
pause(2)

% now add more echos
new_length = length(x4) + n_delay + n_delay;
x4_first_term = [x4 zeros(1, n_delay) zeros(1, n_delay)];
x4_second_term = [zeros(1, n_delay) x4 zeros(1, n_delay)];
x4_third_term = [zeros(1, n_delay) zeros(1, n_delay) x4];

x4_echo = x4_first_term + 0.5*x4_second_term + 0.25*x4_third_term;
sound(x4_echo, Fs)

