#!/usr/bin/python3
import numpy as np
from scipy import fft

rate = 512

t = np.linspace(0, 1, rate, endpoint=False)

def cosf(f, a = 1.0, p=0.0):
    return a * np.cos(2 * np.pi * f * t + p)

s1 = cosf(10)
s2 = cosf(20, 2.0, np.pi / 2)
x = s1 + s2

yf = fft.rfft(x) / (0.5 * rate)

def mag_phase():
    for i, y in enumerate(yf):
        m = abs(y)
        if m > 0.001:
            print(i, m, np.angle(y))

def fft_err():
    x2 = fft.irfft(yf * 0.5 * rate)
    for y1, y2 in zip(x, x2):
        print(y1 - y2)

yf2 = np.zeros(rate)
yf2[10] = 0.5 * rate
yf2[20] = 0.5 * rate
x2 = fft.irfft(yf2)
for i, y in enumerate(x2):
    print(i / rate, y)
