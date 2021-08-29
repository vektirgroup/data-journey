import streamlit as st
import numpy as np
import pandas as pd

# Set initial app configs
st.set_page_config(
   page_title="Data Journey App",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

df1 = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20))
)

my_table = st.table(df1)