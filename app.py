from streamlit_dashboard import data_exploration_part_I, \
    data_exploration_part_II
import streamlit as st
from scripts.multiapp import MultiApp

st.set_page_config(page_title="Rossmann Pharmaceutical Sales Prediction", layout="wide")

app = MultiApp()
st.sidebar.markdown("""
### Rossmann Pharmaceutical Sales Prediction
""")

# Add all your application here
app.add_app("Exploratory Data Analysis Part I", data_exploration_part_I.app)
app.add_app("Exploratory Data Analysis Part II", data_exploration_part_II.app)

# The main app
app.run()
