import streamlit as st
import pandas as pd


def app():
    st.subheader("Mean Sales in the 5 Competition Distance Decile Classes")
    st.image('./images/mean_sales_in_decile_classess.png')

    st.subheader("Competition Distance")
    st.image('./images/competition_distance.png')

    st.subheader("Seasonality Averaged Daily")
    st.image('./images/seasonality_plot.png')

    st.subheader("Seasonality Averaged Weekly")
    st.image('./images/seasonality_plot_weekly.png')

    st.subheader("Seasonality Averaged Monthly")
    st.image('./images/seasonality_plot_monthly.png')

    st.subheader("Seasonality Averaged Year")
    st.image('./images/seasonality_plot_yearly.png')

    st.subheader("Sales Distribution")
    st.image('./images/sales_distribution.png')

    st.subheader("Sales")
    st.image('./images/sales_box_plot.png')

    st.subheader("Customer")
    st.image('./images/customers_box_plot.png')

    st.subheader("Closest Competition")
    st.image('./images/closest_competition_box_plot.png')

