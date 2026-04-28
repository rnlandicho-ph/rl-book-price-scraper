import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/books.csv")

col1, col2 = st.columns([1, 4])

with col1:
    st.image("assets/RLscrapingservices.png", width=200)

with col2:
    st.title("Book Price Dashboard")

st.divider()

st.subheader("📊 Summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books:", len(df))
col2.metric("Average Price: £", round(df["Price (£)"].mean(), 2))
col3.metric("Max Price: £", df["Price (£)"].max())
col4.metric("Min Price: £", df["Price (£)"].min())

st.divider()

search = st.text_input("Search book title")
if search:
    filtered_title_df = df[df["Title"].str.contains(search, case=False)]
    st.write(filtered_title_df)

st.divider()

st.subheader("🔍 Filter by Price")
min_price = st.slider("Minimum price", 0, 100, 0)
filtered_price_df = df[df["Price (£)"] >= min_price]
st.write(filtered_price_df)

st.divider()

st.subheader("🔍 Filter by Availability")
availability = st.selectbox("Select availability", df["Availability"].unique())
filtered_df = df[df["Availability"] == availability]
st.write(filtered_df)

st.divider()

if st.checkbox("Show raw data"):
    st.write(df)