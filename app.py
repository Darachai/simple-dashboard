import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Student Dashboard", layout="wide")

st.title("Student Performance Dashboard")
st.write("Dashboard version 1.2")


# Generate Sample Data

np.random.seed(42)
data = pd.DataFrame({
    "Year": np.random.choice([1, 2, 3, 4], 200),
    "Gender": np.random.choice(["Male", "Female"], 200),
    "GPA": np.random.normal(3.0, 0.4, 200),
    "Department": np.random.choice(["AI", "IT", "CS"], 200)
})


# Filters

year_selected = st.selectbox("Select Year", sorted(data["Year"].unique()))

dept_selected = st.multiselect(
    "Select Department",
    data["Department"].unique(),
    default=data["Department"].unique()
)

with st.sidebar:
    st.header("Filters")
    year_selected = st.selectbox("Select Year", sorted(data["Year"].unique()))

    dept_selected = st.multiselect(
        "Select Department",
        data["Department"].unique(),
        default=data["Department"].unique()
    )

st.divider()
# KPI Section

col_kpi1, col_kpi2 = st.columns(2)

with col_kpi1:
    st.metric("Total Students", len(filtered_data))

with col_kpi2:
    st.metric("Average GPA", round(filtered_data["GPA"].mean(), 2))
st.divider()

# Charts

st.subheader("GPA Distribution")
fig1 = px.histogram(
    filtered_data,
    x="GPA",
    nbins=15,
    color_discrete_sequence=["#4F8BF9"]
)

st.subheader("Gender Distribution")
fig2 = px.pie(
    filtered_data,
    names="Gender",
    color_discrete_sequence=["#4F8BF9", "#FF6B6B"]
)

st.subheader("Department Distribution")

dept_count = filtered_data["Department"].value_counts().reset_index()
dept_count.columns = ["Department", "Count"]

fig3 = px.bar(
    dept_count,
    x="Department",
    y="Count",
    color_discrete_sequence=["#6BCB77"]
)

# Layout
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)

st.plotly_chart(fig3, use_container_width=True)

st.caption("This dashboard visualizes student performance based on selected filters.")