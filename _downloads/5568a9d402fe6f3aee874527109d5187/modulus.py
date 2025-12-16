# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 08:49:35 2023

@author: george.york
"""

# example of using modulus to find aliased frequencies
#  Assume input frequencies are floats (not ints)
Fs = 1500.0
print("If Fs  = ", Fs)
Fin = 250.0
print("If Fin  = ", Fin)
Aliased250 = ((Fin + Fs/2) % Fs) - (Fs/2)
print("Aliased250   = ", Aliased250)

Fin = 450.0
print("If Fin  = ", Fin)
Aliased450 = ((Fin + Fs/2) % Fs) - (Fs/2)
print("Aliased450   = ", Aliased450)

Fin = 1000.0
print("If Fin = ", Fin)
Aliased1000 = ((Fin + Fs/2) % Fs) - (Fs/2)
print("Aliased1000 = ", Aliased1000)

Fin = 2750.0
print("If Fin = ", Fin)
Aliased2750 = ((Fin + Fs/2) % Fs) - (Fs/2)
print("Aliased2750 = ", Aliased2750)

Fin = 4050.0
print("If Fin = ", Fin)
Aliased4050 = ((Fin + Fs/2) % Fs) - (Fs/2)
print("Aliased4050 = ", Aliased4050)

