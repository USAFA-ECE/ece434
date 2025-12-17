# import libraries
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def win_ana2(x1, n1, x2, n2):
    
    # Analysis of signals with various windows
    # function win_ana2(n1, n2, x1, x2)
    # x1 from Porat p. 185
    #
    # recommended use:
    #   >> load windat
    #   >> win_ana2
    #
    #n1=0:127;
    #x1=sin(0.3984*pi*n1)+(0.005*sin(0.5*pi*n1));
    # x2 from Proakis/Manolakis (3rd ed) p. 435
    #n2=0:127;
    #x2=cos(0.2*pi*n2)+cos(0.22*pi*n2)+cos(0.6*pi*n2);
    # save the data such that version 4 can read it too
    #save cx1a_dat Fs n1 x1 n2 x2 n3 x3 -v4;
    
    # Analysis of first signal
    # Window the data
    #x1bart=x1.*transpose(window(@bartlett,128));
    from scipy.signal import bartlett, hann, hamming, blackman, kaiser
    x1bart=x1*(bartlett(128))
    x1hann=x1*(hann(128)) 
    x1hamm=x1*(hamming(128))  
    x1blac=x1*(blackman(128))  
    x1kais=x1*(kaiser(128, 10))  
    # x1dolp=x1*(hann,128));   window(128,'dolp',-80);
    X1=np.fft.fft(x1); # equivalent to using rect window
    X1bart=np.fft.fft(x1bart);
    X1hann=np.fft.fft(x1hann);
    X1hamm=np.fft.fft(x1hamm);
    X1blac=np.fft.fft(x1blac);
    X1kais=np.fft.fft(x1kais);
    # X1dolp=fft(x1dolp);
    # Try zero padding out to 512
    x1z=np.concatenate((x1, np.zeros(384)))
    x1bartz=np.concatenate((x1bart, np.zeros(384)))
    x1hannz=np.concatenate((x1hann, np.zeros(384)))
    x1hammz=np.concatenate((x1hamm, np.zeros(384)))
    x1blacz=np.concatenate((x1blac, np.zeros(384)))
    x1kaisz=np.concatenate((x1kais, np.zeros(384)))
    # x1dolpz=[x1dolp, zeros(1,384)];
    X1z=np.fft.fft(x1z)
    X1bartz=np.fft.fft(x1bartz)
    X1hannz=np.fft.fft(x1hannz)
    X1hammz=np.fft.fft(x1hammz)
    X1blacz=np.fft.fft(x1blacz)
    X1kaisz=np.fft.fft(x1kaisz)
    # X1dolpz=fft(x1dolpz);
    # Plot the first signal
    plt.figure(1)
    plt.subplot(221)
    plt.plot(np.arange(0,65),20*np.log10(np.abs(X1[0:65])/np.max(np.abs(X1))))
    plt.xlabel('rect')
    plt.subplot(222)
    plt.plot(np.arange(0,65),20*np.log10(np.abs(X1bart[0:65])/np.max(np.abs(X1bart))))
    plt.xlabel('Bartlett')
    plt.subplot(223)
    plt.plot(np.arange(0,65),20*np.log10(np.abs(X1hann[0:65])/np.max(np.abs(X1hann))))
    plt.xlabel('von Hann')
    plt.subplot(224)
    plt.plot(np.arange(0,65),20*np.log10(np.abs(X1hamm[0:65])/np.max(np.abs(X1hamm))))
    plt.xlabel('Hamming')
    plt.show()
    plt.figure(2)
    plt.subplot(221)
    plt.plot(np.arange(0,65),20*np.log10(np.abs(X1blac[0:65])/np.max(np.abs(X1blac))))
    plt.xlabel('Blackman')
    plt.subplot(222)
    plt.plot(np.arange(0,65),20*np.log10(np.abs(X1kais[0:65])/np.max(np.abs(X1kais))))
    plt.xlabel('Kaiser, alpha=10')
    plt.subplot(223)
    # plot(0:64,20*np.log10(np.abs(X1dolp(np.arange(1:66)))/max(abs(X1dolp))));
    # plt.xlabel('Dolph, alpha=-80')
    plt.show()
    
    plt.figure(3)
    plt.subplot(221)
    plt.plot(np.arange(0,257),20*np.log10(np.abs(X1z[0:257])/np.max(np.abs(X1z))));
    plt.xlabel('rect')
    plt.subplot(222)
    plt.plot(np.arange(0,257),20*np.log10(np.abs(X1bartz[0:257])/np.max(np.abs(X1bartz))));
    plt.xlabel('Bartlett')
    plt.subplot(223)
    plt.plot(np.arange(0,257),20*np.log10(np.abs(X1hannz[0:257])/np.max(np.abs(X1hannz))));
    plt.xlabel('von Hann')
    plt.subplot(224)
    plt.plot(np.arange(0,257),20*np.log10(np.abs(X1hammz[0:257])/np.max(np.abs(X1hammz))));
    plt.xlabel('Hamming')
    plt.show()
    plt.figure(4)
    plt.subplot(221)
    plt.plot(np.arange(0,257),20*np.log10(np.abs(X1blacz[0:257])/np.max(np.abs(X1blacz))));
    plt.xlabel('Blackman')
    plt.subplot(222)
    plt.plot(np.arange(0,257),20*np.log10(np.abs(X1kaisz[0:257])/np.max(np.abs(X1kaisz))));
    plt.xlabel('Kaiser, alpha=10')
    plt.subplot(223)
    # plot(0:256,20*np.log10(np.abs(X1dolpz(1:257))/max(abs(X1dolpz))));
    # plt.xlabel('Dolph, alpha=-80')
    plt.show()
    
    # Analysis of second signal
    # Window the data
    k2=len(x2)
    
    x2bart=x2*(bartlett(k2))
    x2hann=x2*(hann(k2))
    x2hamm=x2*(hamming(k2))
    x2blac=x2*(blackman(k2))
    x2kais=x2*(kaiser(k2,10)) 
    # x2dolp=x2.*window(k2,'dolp',-80);
    X2=np.fft.fft(x2) # equivalent to using rect window
    X2bart=np.fft.fft(x2bart)
    X2hann=np.fft.fft(x2hann)
    X2hamm=np.fft.fft(x2hamm)
    X2blac=np.fft.fft(x2blac)
    X2kais=np.fft.fft(x2kais)
    # X2dolp=fft(x2dolp);
    # Try zero padding out to 2048
    zz=2048-k2
    x2z=np.concatenate((x2, np.zeros(zz)))
    x2bartz=np.concatenate((x2bart, np.zeros(zz)))
    x2hannz=np.concatenate((x2hann, np.zeros(zz)))
    x2hammz=np.concatenate((x2hamm, np.zeros(zz)))
    x2blacz=np.concatenate((x2blac, np.zeros(zz)))
    x2kaisz=np.concatenate((x2kais, np.zeros(zz)))
    # x2dolpz=[x2dolp, zeros(1,zz)];
    X2z=np.fft.fft(x2z)
    X2bartz=np.fft.fft(x2bartz)
    X2hannz=np.fft.fft(x2hannz)
    X2hammz=np.fft.fft(x2hammz)
    X2blacz=np.fft.fft(x2blacz)
    X2kaisz=np.fft.fft(x2kaisz)
    # X2dolpz=fft(x2dolpz);
    # Plot the second signal
    k22=int(k2/2)
    plt.figure(5)
    plt.subplot(221)
    plt.plot(np.arange(0,k22),20*np.log10(np.abs(X2[0:k22])/np.max(np.abs(X2))))
    plt.xlabel('rect')
    plt.subplot(222)
    plt.plot(np.arange(0,k22),20*np.log10(np.abs(X2bart[0:k22])/np.max(np.abs(X2bart))))
    plt.xlabel('Bartlett')
    plt.subplot(223)
    plt.plot(np.arange(0,k22),20*np.log10(np.abs(X2hann[0:k22])/np.max(np.abs(X2hann))))
    plt.xlabel('von Hann')
    plt.subplot(224)
    plt.plot(np.arange(0,k22),20*np.log10(np.abs(X2hamm[0:k22])/np.max(np.abs(X2hamm))))
    plt.xlabel('Hamming')
    plt.show()
    
    plt.figure(6)
    plt.subplot(221)
    plt.plot(np.arange(0,k22),20*np.log10(np.abs(X2blac[0:k22])/np.max(np.abs(X2blac))));
    plt.xlabel('Blackman')
    plt.subplot(222)
    plt.plot(np.arange(0,k22),20*np.log10(np.abs(X2kais[0:k22])/np.max(np.abs(X2kais))));
    plt.xlabel('Kaiser, alpha=10')
    plt.subplot(223)
    # plot(0:k22,20*np.log10(np.abs(X2dolp(1:k22+1))/max(abs(X2dolp))));
    # plt.xlabel('Dolph, alpha=-80')
    plt.show()
    
    plt.figure(7)
    k2z=int(len(X2z)/2)
    plt.subplot(221)
    plt.plot(np.arange(0,k2z),20*np.log10(np.abs(X2z[0:k2z])/np.max(np.abs(X2z))));
    plt.xlabel('rect')
    plt.subplot(222)
    plt.plot(np.arange(0,k2z),20*np.log10(np.abs(X2bartz[0:k2z])/np.max(np.abs(X2bartz))));
    plt.xlabel('Bartlett')
    plt.subplot(223)
    plt.plot(np.arange(0,k2z),20*np.log10(np.abs(X2hannz[0:k2z])/np.max(np.abs(X2hannz))));
    plt.xlabel('von Hann')
    plt.subplot(224)
    plt.plot(np.arange(0,k2z),20*np.log10(np.abs(X2hammz[0:k2z])/np.max(np.abs(X2hammz))));
    plt.xlabel('Hamming')
    plt.show()
    
    plt.figure(8)
    plt.subplot(221)
    plt.plot(np.arange(0,k2z),20*np.log10(np.abs(X2blacz[0:k2z])/np.max(np.abs(X2blacz))));
    plt.xlabel('Blackman')
    plt.subplot(222)
    plt.plot(np.arange(0,k2z),20*np.log10(np.abs(X2kaisz[0:k2z])/np.max(np.abs(X2kaisz))));
    plt.xlabel('Kaiser, alpha=10')
    plt.subplot(223)
    # plot(0:k2z,20*log10(abs(X2dolpz(1:k2z+1))/max(abs(X2dolpz))));
    # plt.xlabel('Dolph, alpha=-80')
    # Plot padded version of second signal on linear scale
    plt.show()
    
    plt.figure(9)
    plt.subplot(221)
    plt.plot(np.arange(0,k2z),abs(X2z[0:k2z])/np.max(np.abs(X2z)));
    plt.xlabel('rect')
    plt.subplot(222)
    plt.plot(np.arange(0,k2z),abs(X2bartz[0:k2z])/np.max(np.abs(X2bartz)));
    plt.xlabel('Bartlett')
    plt.subplot(223)
    plt.plot(np.arange(0,k2z),abs(X2hannz[0:k2z])/np.max(np.abs(X2hannz)));
    plt.xlabel('von Hann')
    plt.subplot(224)
    plt.plot(np.arange(0,k2z),abs(X2hammz[0:k2z])/np.max(np.abs(X2hammz)));
    plt.xlabel('Hamming')
    plt.figure(10)
    plt.subplot(221)
    plt.plot(np.arange(0,k2z),abs(X2blacz[0:k2z])/np.max(np.abs(X2blacz)));
    plt.xlabel('Blackman')
    plt.subplot(222)
    plt.plot(np.arange(0,k2z),abs(X2kaisz[0:k2z])/np.max(np.abs(X2kaisz)));
    plt.xlabel('Kaiser, alpha=10')
    plt.subplot(223)
    # plot(0:k2z,abs(X2dolpz(1:k2z+1))/max(abs(X2dolpz)));
    # plt.xlabel('Dolph, alpha=-80')
    plt.show()
    
    #figure(1)
    
    return