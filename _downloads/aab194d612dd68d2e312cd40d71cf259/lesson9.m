% code from lesson 9
% by George York

%estimating comp time for DFT versus FFT
% assume DFT has initial overhead of 5 ops and FFT has initial overhead of
% 20 ops

n=1:8;
plot(n, n.*n + 5, n, n.*log2(n) + 20);

n=1:64;
plot(n, n.*n + 5, n, n.*log2(n) + 20);

n=1:1024;
plot(n, n.*n + 5, n, n.*log2(n) + 20);
