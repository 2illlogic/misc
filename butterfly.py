import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import norm, beta
#from quantecon import LAE
from scipy.stats import norm, gaussian_kde

r=np.linspace(np.random.normal(0,1),100)
theta=np.linspace(np.random.normal(0,1),100)

a=norm(0,1)
n=2
T=20

k = np.empty((n,T))
A = a.rvs((n,T)) 
k[:, 0] = [0, 0]
for t in range(T-1):
   k[:, t+1] = A[:, t] + k[:, t]

fig, ax = plt.subplots()
ax.scatter(k[0], k[1])
ax.plot(k[0], k[1])
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data',0))
#ax.set_xlim([-10,10])
#ax.set_ylim([-10,10])      
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

l = np.empty(T)
l[0]=0
for t in range(1, T):
   l[t] = np.sqrt((k[0, t]-k[0, t-1])**2 + (k[1, t]-k[1, t-1])**2)

np.sum(l)
l
k
y_bd=max(abs(min(k[1])),abs(max(k[1])))

a.cdf(0)
a.pdf(0)

k
l
