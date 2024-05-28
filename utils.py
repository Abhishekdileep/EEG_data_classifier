import mne 
import numpy as np 
import glob 

    
def patient_list_raw(path):
    healthy_list = []
    epiliptic_list = []
    category = [ 'Healthy' , 'Epileptic' ] 
    for type in category : 
        for name in glob.glob('{0}/{1}/*.fif'.format(path , type)): 
            data = mne.io.read_raw_fif(name , preload = True)  
            if type == 'Healthy' : healthy_list.append(data) 
            else : epiliptic_list.append(data)
    return healthy_list , epiliptic_list

def patient_list_info(path):
    healthy_list = []
    epiliptic_list = []
    category = [ 'Healthy' , 'Epileptic' ] 
    for type in category : 
        for name in glob.glob('{0}/{1}/*.fif'.format(path , type)): 
            data = mne.io.read_info(name , verbose = True)  
            if type == 'Healthy' : healthy_list.append(data) 
            else : epiliptic_list.append(data)
    return healthy_list , epiliptic_list

# def read_file(patient_list):
#     time_list = []
#     amplitude_list = []
#     for i in patient_list : 
#         raw = import_fif(i)
#         time_list = raw.get_times
def Get_Np_Signal( raw_data):
    elip_data = raw_data.get_data().T # Transpose for channel-wise data
    return elip_data