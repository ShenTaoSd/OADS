import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

plt.rcParams['font.family'] = 'Bitstream Vera Sans'
plt.rcParams['text.hinting'] = False
plt.rcParams['text.hinting_factor'] = 8

# 产生分布
fit = plt.figure()

figa = plt.gca()

N = 100
xn = np.random.rand(100)
x = np.linspace(0, 1)

a = np.random.rand()
b = np.random.rand()

f = x * a + b;
plt.plot(x, f, 'r')
