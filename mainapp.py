# -*- coding: utf-8 -*-
"""
@author: rashmi
"""

import numpy as np
import pickle
import streamlit as st
from webapp import main

if __name__=="__main__":
        main()



st.sidebar.selectbox("Explore/Predict","predict","Explore")