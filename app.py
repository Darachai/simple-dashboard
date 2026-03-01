import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD IMAGE FUNCTION ----------------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img1 = get_base64("images.jpg")
img2 = get_base64("who-wins-heian-sukuna-or-four-arms-v0-8u28q2n56gle1.webp")

# ---------------- CINEMATIC IMAGE SECTION ----------------
st.markdown(f"""
<style>
.cinema-container {{
    display: flex;
    gap: 40px;
    margin-bottom: 40px;
}}

.cinema-img {{
    width: 100%;
    border-radius: 25px;
    box-shadow: 0px 20px 60px rgba(0,0,0,0.8);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}}

.cinema-img:hover {{
    transform: scale(1.05);
    box-shadow: 0px 30px 80px rgba(0,0,0,1);
}}
</style>

<h1>🎓 Student Performance Dashboard</h1>
<p style="color:gray;">Dashboard version 6.0 - Cinematic Edition</p>

<div class="cinema-container">
    <img class="cinema-img" src="data:image/jpg;base64,{img1}">
    <img class="cinema-img" src="data:image/webp;base64,{img2}">
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------- GENERATE DATA ----------------
np.random.seed(42)
data = pd.DataFrame({
    "Year": np.random.choice([1, 2, 3, 4], 200),
    "Gender": np.random.choice(["Male", "Female"], 200),
    "GPA": np.random.normal(3.0, 0.4, 200),
    "Department": np.random.choice(["AI", "IT", "CS"], 200)
})

# ---------------- SIDEBAR FILTERS ----------------
with st.sidebar:
    st.header("Filters")

    year_selected = st.selectbox(
        "Select Year",
        sorted(data["Year"].unique())
    )

    dept_selected = st.multiselect(
        "Select Department",
        data["Department"].unique(),
        default=data["Department"].unique()
    )

    if st.button("Reset Filters"):
        st.rerun()

# ---------------- FILTER DATA ----------------
filtered_data = data[
    (data["Year"] == year_selected) &
    (data["Department"].isin(dept_selected))
].copy()

# ---------------- GPA CATEGORY ----------------
def categorize_gpa(gpa):
    if gpa < 2.5:
        return "Low"
    elif gpa < 3.25:
        return "Medium"
    else:
        return "High"

filtered_data["GPA Level"] = filtered_data["GPA"].apply(categorize_gpa)

# ---------------- KPI SECTION ----------------
st.subheader("📊 Summary Statistics")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Students", len(filtered_data))

with col2:
    st.metric("Average GPA", round(filtered_data["GPA"].mean(), 2))

# ---------------- GAUGE ----------------
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

# ---------------- SUMMARY TABLE ----------------
summary = filtered_data[["GPA"]].describe()
st.dataframe(summary)

# ---------------- DOWNLOAD CSV ----------------
csv = filtered_data.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_students.csv",
    mime="text/csv"
)

st.divider()

# ---------------- CHARTS ----------------
st.markdown("## 📈 GPA Distribution")
fig1 = px.histogram(filtered_data, x="GPA", nbins=15)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("## 👥 Gender Distribution")
fig2 = px.pie(filtered_data, names="Gender")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("## 🏫 Department Distribution")
dept_count = filtered_data["Department"].value_counts().reset_index()
dept_count.columns = ["Department", "Count"]

fig3 = px.bar(dept_count, x="Department", y="Count")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("## 📊 GPA Level Distribution")
gpa_level_count = filtered_data["GPA Level"].value_counts().reset_index()
gpa_level_count.columns = ["Level", "Count"]

fig4 = px.bar(gpa_level_count, x="Level", y="Count")
st.plotly_chart(fig4, use_container_width=True)

st.divider()
st.markdown("© 2025 Student Performance Dashboard | Developed with Streamlit")