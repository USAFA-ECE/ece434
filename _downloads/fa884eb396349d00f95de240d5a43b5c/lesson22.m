% demo of instability due to quantization effects
cd qfilt
load filt1
filt1
filt1.tf
filt1.tf.num
qfilt


% plots for class example
b = [0.5 -0.6 0.3]
a = [1 -0.7 0.4]
[z, p, k] = tf2zp(b,a)
zplane(b,a)
freqz(b,a)
