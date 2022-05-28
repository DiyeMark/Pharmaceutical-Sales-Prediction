import streamlit as st
import pandas as pd


def app():
    st.title("Exploratory Data Analysis Part I")

    st.subheader("Top 6 features with highest correlation with sales")
    st.image('./images/correlation_map.png')

    st.subheader("State Holidays")
    st.image('./images/state_holiday.png')

    st.subheader("Sales During State Holidays")
    st.image('./images/sales_during_state_holiday.png')

    st.subheader("Customers During State Holidays")
    st.image('./images/customers_during_holidays.png')

    st.subheader("Store Type")
    st.image('./images/store_type_count.png')

    st.subheader("Sales and Customers Across Store Type")
    st.image('./images/customers_across_store_type.png')

    st.subheader("Assortment Type")
    st.image('./images/assortment_type_count.png')

    st.subheader("Sales and Customers Across Assortment Type")
    st.image('./images/customers_across_assortment.png')

    st.subheader("Store Open Status Across Different Days of the Week")
    st.image('./images/store_open.png')

    st.subheader("Sales and Customers Across Different Days of the Week")
    st.image('./images/customers_across_different_days.png')

    st.subheader("Weekday")
    st.image('./images/weekday.png')

    st.subheader("Sales and Customers During Weekends vs Weekdays")
    st.image('./images/customers_during_weekend.png')

    st.subheader("Promo")
    st.image('./images/promo_count.png')

    st.subheader("Sales and Customers Across Different Promo")
    st.image('./images/customer_across_promo.png')
