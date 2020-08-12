import scipy.signal
import numpy as np

# 04/27/20 12:02AM
# Attempt at low-pass filtering

f = 100 # w=2*pi*f
x = np.linspace(0, 0.1, 1000)
y = np.sin(2*np.pi*f*x) + 2.1 * np.random.rand(len(x))

sos = scipy.signal.butter(1, 2*np.pi*110, analog=True, output="sos")
yf = scipy.signal.sosfilt(sos, y)
