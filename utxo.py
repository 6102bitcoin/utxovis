import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
import pandas as pd
import csv
import pickle
import os

# SELECT MODE
print("SELECT MODE:")
print("A | Test Mode (10s runtime)")
print("B | Real Mode (10 mins)")
mode = input("Select Mode (Type A or B): ")

if mode == "A" or mode == "a":
    filename = "utxodump-demo.csv"
    # Generate testfile from utxodump.csv
    testfile = []
    count = 0
    for chunk in pd.read_csv('utxodump.csv', chunksize=100000):
        if count < 1:
            testfile = chunk
            count = count + 1
            # print(chunk)
        else:
            break
    testfile.to_csv(filename, index=False)

if mode == "B" or mode == "b":
    filename = "utxodump.csv"


file_size = os.path.getsize(os.getcwd() + '/' + str(filename))
estimated_utxo_count = int(file_size / 122)

print("Found approx " + str(estimated_utxo_count) + " utxos")

chunksize_value = 1000000
loops = estimated_utxo_count/chunksize_value
progress_per_loop_percent = 100 / loops

utxo_sizes_set = set()
utxo_sizes_dict = dict()


print("Progress:")
print("0 %")

progress = 0
for chunk in pd.read_csv(str(filename), chunksize=chunksize_value):
    for value in chunk["amount"]:
        if value in utxo_sizes_set:
            utxo_sizes_dict[value]+= 1
        else: 
            utxo_sizes_set.add(value)
            utxo_sizes_dict[value]= 1
    progress = int(progress + progress_per_loop_percent)
    print(str(progress) + " %")

print("Sorting Data")

lists = sorted(utxo_sizes_dict.items()) 
utxo_size, count = zip(*lists)

print("Saving Data")

with open('utxo_size.pkl', 'wb') as f:
    pickle.dump(utxo_size, f)

with open('count.pkl', 'wb') as f:
    pickle.dump(count, f)

print("Data Saved")

