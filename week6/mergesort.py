import numpy as np   

def mergesort(a):
    aux = np.copy(a)
    sort(a,0,len(a)-1, aux)
    return a


def sort(a, low, high, aux):
    
    # Base case: nothing to do
    if (high <= low): 
        return
    
    # Find the midpoint
    mid = low + int(np.floor(((high - low) / 2)))   
    
    # Divide and Conquer using Recursion!
    sort(a, low, mid, aux)      # Sort left half  
    sort(a, mid+1, high, aux)   # Sort right half
    
    # Merge left and right halves
    merge(a, low, mid, high, aux)

def merge(a, low, mid, high, aux):
    
    i = int(low)
    j = int(mid + 1)
    
    # Make a copy
    aux[low:high+1] = a[low:high+1]
    
    # Merge two arrays
    k = int(low)
    while (k <= high):
        while ( (i <= mid) & (j <= high) ):
            if ( aux[j] < aux[i] ):
                a[k] = aux[j]
                j += 1
                k += 1
            else:
                a[k] = aux[i]
                i += 1
                k += 1
        # Now either i > mid or j > high
        # So only one of below loops will run
        while (i <= mid):
            a[k] = aux[i]
            i += 1
            k += 1
        while (j <= high):
            a[k] = aux[j]
            j += 1
            k += 1