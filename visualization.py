import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("📊 Student Data Analysis Dashboard")

# Load data
data = pd.read_csv("data.csv")

# Show dataset
st.subheader("Dataset")
st.write(data)

# Create Average column
data["Average"] = (
    data["Math"] + data["Science"] + data["English"]
) / 3

# ---------------- BAR CHART ----------------
st.subheader("Bar Chart - Student Average Marks")

fig1, ax1 = plt.subplots()
ax1.bar(data["Name"], data["Average"])
ax1.set_xlabel("Students")
ax1.set_ylabel("Average Marks")
ax1.set_title("Student Average Marks")

st.pyplot(fig1)

# ---------------- PIE CHART ----------------
st.subheader("Pie Chart - Subject Distribution")

subjects = ["Math", "Science", "English"]
avg_marks = data[subjects].mean()

fig2, ax2 = plt.subplots()
ax2.pie(avg_marks, labels=subjects, autopct='%1.1f%%')
ax2.set_title("Subject Distribution")

st.pyplot(fig2)

# ---------------- SCATTER PLOT ----------------
st.subheader("Scatter Plot - Study Hours vs Average Marks")

fig3, ax3 = plt.subplots()
ax3.scatter(data["StudyHours"], data["Average"])
ax3.set_xlabel("Study Hours")
ax3.set_ylabel("Average Marks")
ax3.set_title("Study Hours vs Average Marks")

st.pyplot(fig3)

# Footer
st.success("Dashboard Loaded Successfully ✅")
