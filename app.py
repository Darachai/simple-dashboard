import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Student Performance Dashboard")
st.image("gojo.png", caption="มหาเวทผนึกมาร", use_container_width=True)
st.write("Dashboard version 1.2")

with st.spinner("Loading dashboard..."):
    st.success("Dashboard loaded successfully!")
# Generate Sample Data

np.random.seed(42)
data = pd.DataFrame({
    "Year": np.random.choice([1, 2, 3, 4], 200),
    "Gender": np.random.choice(["Male", "Female"], 200),
    "GPA": np.random.normal(3.0, 0.4, 200),
    "Department": np.random.choice(["AI", "IT", "CS"], 200)
})
csv = filtered_data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_students.csv",
    mime="text/csv"
)

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
def categorize_gpa(gpa):
    if gpa < 2.5:
        return "Low"
    elif gpa < 3.25:
        return "Medium"
    else:
        return "High"

filtered_data["GPA Level"] = filtered_data["GPA"].apply(categorize_gpa)    

st.divider()
# KPI Section
st.subheader("Summary Statistics")

summary = filtered_data[["GPA"]].describe()
st.dataframe(summary)

col_kpi1, col_kpi2 = st.columns(2)

with col_kpi1:
    st.metric("Total Students", len(filtered_data))

with col_kpi2:
    st.metric("Average GPA", round(filtered_data["GPA"].mean(), 2))

st.divider()
import plotly.graph_objects as go

avg_gpa = round(filtered_data["GPA"].mean(), 2)

gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=avg_gpa,
    title={'text': "Average GPA"},
    gauge={
        'axis': {'range': [0, 4]},
        'bar': {'color': "#4F8BF9"}
    }
))

st.plotly_chart(gauge, use_container_width=True)

if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_data)
# Charts
gpa_level_count = filtered_data["GPA Level"].value_counts().reset_index()
gpa_level_count.columns = ["Level", "Count"]

fig_gpa_level = px.bar(
    gpa_level_count,
    x="Level",
    y="Count",
    color_discrete_sequence=["#FFA500"]
)

st.plotly_chart(fig_gpa_level, use_container_width=True)

st.markdown("## 📈 GPA Distribution")
fig1.update_traces(
    hovertemplate="GPA: %{x}<br>Count: %{y}"
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
dept_count = dept_count.sort_values("Count", ascending=False)

gender_count = filtered_data["Gender"].value_counts().reset_index()
gender_count.columns = ["Gender", "Count"]

fig_gender_bar = px.bar(
    gender_count,
    x="Gender",
    y="Count",
    color_discrete_sequence=["#FF6B6B"]
)

st.plotly_chart(fig_gender_bar, use_container_width=True)

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
with st.expander("View Special Image"):
    st.image("gojo.png", caption="มหาเวทผนึกมาร", use_container_width=True)

st.caption("This dashboard visualizes student performance based on selected filters.")
st.divider()
st.markdown("© 2025 Student Performance Dashboard | Developed with Streamlit")