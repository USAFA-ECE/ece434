function DFT_demo(fo, Fs, N)
% example use:  DFT_demo(100,800,8)
% demos an N-point DFT of a fo Hz sinusoid sampled at Fs Hz. 
% Pauses between each calculation


nn = 0:(N-1);
i = 1:N;
x(i) = cos(2*pi*(fo/Fs)*nn);
%real_mult(i)=0;
%imag_mult(i)=0;
DFT_bins(i)=0;
figure(1)
subplot(4,2,1)
stem(nn,x)
xlabel('n')
ylabel('x[n]')
for k = 0:(N-1)
    k
    real_mult(i)=0;
    imag_mult(i)=0;
    k_sum = 0 + j*0;
    for n = 0:(N-1)
        n
        W = exp(-j*2*pi*k*n/N);
        subplot(4,2,2)
        compass(W)
        xlabel('phasor W')
        subplot(4,2,3)
        real_mult(n+1)=real(x(n+1)*W);
        stem(nn,real_mult, 'r')
        xlabel('n')
        ylabel('Real(x[n]*W)')
        %subplot(4,2,4)
        %compass(real(W))
        subplot(4,2,5)
        imag_mult(n+1)=imag(x(n+1)*W);
        stem(nn,imag_mult, 'r')
        xlabel('n')
        ylabel('Imag(x[n]*W)')
        %subplot(4,2,6)
        %compass(imag(W))
        k_sum = k_sum + x(n+1)*W;
        
        pause
    end
    subplot(4,2,7)
    DFT_bins(k+1)= abs(k_sum);
    stem(nn,DFT_bins);
    xlabel('k')
    ylabel('DFT')
    pause
end

