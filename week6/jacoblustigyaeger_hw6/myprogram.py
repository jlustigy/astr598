#!/usr/bin/python

import timeit
import numpy as np
from mergesort import mergesort
import matplotlib.pyplot as plt
from matplotlib import gridspec

def time_mergesort(N):
    # Initialize array of random numbers between 0 and N with length N 
    a = np.random.randint(low=0,high=int(N),size=int(N))

    # Define timed mergesort object, t
    t = timeit.Timer(lambda: mergesort(a))

    # Run t once and return time
    return t.timeit(number=1)

def run_mergesort(N):
    # Initialize array of random numbers between 0 and N with length N 
    a = np.random.randint(low=0,high=int(N),size=int(N))

    # Run mergesort on a
    return a, mergesort(a)

def time_grid():
    
    # Define Grid of N's
    N = [1e2, 1e4, 1e6, 1e8]

    # Define array to hold times
    times = np.zeros([len(N), 3])

    # For each array length
    for i in range(len(N)):
        # For 3 trials
        for j in range(3):
            # Store mergesort runtime
            times[i,j] = time_mergesort(N[i])
    
    # Calculate average time for the three trials
    return np.mean(times, axis=1)

def plot_results():
    
    avgt = time_grid()
    
    # Plot results
    fig = plt.figure(figsize=(15,10))
    gs = gridspec.GridSpec(1, 1) 
    ax0 = plt.subplot(gs[0])
    ax0.plot(N * np.log10(N), avgt, 'o')
    ax0.set_xlabel('NlogN')
    ax0.set_ylabel('Time (s)')
    ax0.set_title('MergeSort')
    ax0.loglog()
    ax0.set_ylim([3e-4,3e4])
    ax0.set_xlim([1e2,3e9])
    fig.savefig('mergesort.pdf')
    fig.show()
    
    
    