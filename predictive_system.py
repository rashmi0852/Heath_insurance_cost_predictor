# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 19:46:33 2022

@author: rashmi
"""

import numpy as np
import pickle

loaded_model=pickle.load(open("C:/Users/rashmi/Desktop/major/trained_model.sav","rb"))


input_data=(31,1,25.74,0,1,0)
#chaging imputdata as numpy array
np_data=np.asarray(input_data)
#reshape array
data_reshape=np_data.reshape(1,-1)
prediction=loaded_model.predict(data_reshape)
print("insurance cost is",prediction)
