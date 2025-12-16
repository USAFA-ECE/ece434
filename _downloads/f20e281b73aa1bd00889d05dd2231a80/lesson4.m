function lesson4()
%% by George York
% copyright (c) 2004 George York
%  Demos effects of quantization error (both rounding and truncating)


% loat in a wav file, talking
x = jello;
% listen
sound(x, 22050)
z = input('this is sound with 8-bits... hit any key to hear what happens when we quantize to 6 bits (rounding)');

% quantize to 6 bits, rounding
% help quant_r
xq = quant_r(x,6);
sound(xq, 22050)
z = input('this is sound with 6-bits... hit any key to hear what happens when we quantize to 3 bits (rounding)');
% quantize to 3 bits, rounding
xq = quant_r(x,3);
sound(xq, 22050)
z = input('this is sound with 3-bits (rounding)... hit any key to hear what happens when we quantize to 3 bits (truncating)');
% quantize to 3 bits, truncating
xq = quant_t(x,3);
sound(xq, 22050)