import matplotlib
from numpy.core.defchararray import endswith
matplotlib.use('Agg')
import matplotlib.pylab as plt
import pandas as pd
import csv
import pickle
from pylab import *


print("importing data")

with open('utxo_size.pkl', 'rb') as f:
    utxo_size = pickle.load(f)

with open('count.pkl', 'rb') as f:
    count = pickle.load(f)

ylimit=int(10**math.ceil(math.log(max(count),10)))

print("making graph")
plt.figure(figsize=(12,6.75), facecolor='#151516') 
plt.suptitle("Bitcoin utxo set size distribution \n by @6102bitcoin", color='#cecabd')

subplot(1,1,1, facecolor='#292a2d')
plt.loglog(utxo_size,count,',',color='#f7931a')
plt.grid(True, color='#cecabd', alpha=0.5, linestyle='dashed', linewidth=0.5)
plt.xlabel("utxo size (sats)", color='#cecabd')
plt.ylabel("Count", color='#cecabd')
tick_params(labelcolor='#cecabd')
plt.savefig('utxovis.png')