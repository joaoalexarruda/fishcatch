import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Fishcatch",
    page_icon="🐟",
)

st.title('Fishcatch')

st.markdown(
    '''
    ## A simple example of linear and polynomial regression using Python and Scikit-learn
by [joaoalexarruda](https://github.com/joaoalexarruda)
    '''
)

st.divider()