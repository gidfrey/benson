#!/usr/bin/env python
# coding: utf-8




# In[1]:



import streamlit as st
st.header("vote program")
C=st. number_input ("enter your age")
if C>=18:
        st.write("eligibility")
elif C<=18:
        st.write("no eligibility")
        


# In[ ]:




