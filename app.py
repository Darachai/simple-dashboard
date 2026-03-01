import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title("Student Performance Dashboard")

st.write("Dashboard version 1.1")
# KPI Section
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1)

with col2:
    st.plotly_chart(fig2)

st.plotly_chart(fig3)
# สร้างข้อมูลตัวอย่าง
np.random.seed(42)
data = pd.DataFrame({
    "Year": np.random.choice([1, 2, 3, 4], 200),
    "Gender": np.random.choice(["Male", "Female"], 200),
    "GPA": np.random.normal(3.0, 0.4, 200),
    "Department": np.random.choice(["AI", "IT", "CS"], 200)
})

# Interactive filter
year_selected = st.selectbox("Select Year", sorted(data["Year"].unique()))

filtered_data = data[data["Year"] == year_selected]
dept_selected = st.multiselect(
    "Select Department",
    data["Department"].unique(),
    default=data["Department"].unique()
)

filtered_data = filtered_data[
    filtered_data["Department"].isin(dept_selected)
]

# Graph 1: GPA Distribution
st.subheader("GPA Distribution")
fig1 = px.histogram(
    filtered_data,
    x="GPA",
    nbins=15,
    color_discrete_sequence=["#4F8BF9"]
)
# Graph 2: Gender Count
st.subheader("Gender Distribution")
fig2 = px.pie(
    filtered_data,
    names="Gender",
    color_discrete_sequence=["#4F8BF9", "#FF6B6B"]
)
# Graph 3: Department Count
st.subheader("Department Distribution")

dept_count = filtered_data["Department"].value_counts().reset_index()
dept_count.columns = ["Department", "Count"]

dept_selected = st.multiselect(
    "Select Department",
    data["Department"].unique(),
    default=data["Department"].unique()
)

filtered_data = filtered_data[filtered_data["Department"].isin(dept_selected)]

fig3 = px.bar(
    dept_count,
    x="Department",
    y="Count",
    color_discrete_sequence=["#6BCB77"]
)

st.plotly_chart(fig3)
st.caption("This chart shows the GPA distribution for the selected year.")