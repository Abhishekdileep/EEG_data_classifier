import numpy as np 
import mne
from utils import patient_list , Get_Np_Signal

healthy , epiliptic = patient_list("F:/Documents/EE531/Project/EEG Data for Project")

eeg_data = Get_Np_Signal(healthy[0])[0]
NUM_BINS= 1000
def calc_bin_index(s, mean, sigma, dont_skip=True): 
    index = int(((s - mean)  / (4*sigma)   + 0.5) * NUM_BINS)
    if dont_skip:
        if index < 0: index = 0
        if index > NUM_BINS - 1: index = NUM_BINS - 1
    return index
def make_histogram(s, mean, sigma):
    a = np.zeros(NUM_BINS, dtype=np.int32)
    skipped = 0
    for value in s:
        index = calc_bin_index(value, mean, sigma, dont_skip=False)
        if index >= 0 and index < NUM_BINS - 1: a[index] += 1
        else: skipped += 1
    print(skipped)
    return a

hist1 = make_histogram(eeg_data, np.mean(eeg_data), np.std(eeg_data))
s_hist1 = np.convolve(hist1, np.array([1,1 , 1, 1])/4)