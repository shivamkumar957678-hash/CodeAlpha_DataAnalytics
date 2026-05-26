import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")

# Create Average column
data["Average"] = (data["Math"] + data["Science"] + data["English"]) / 3

# 1. Bar Chart
plt.figure()
plt.bar(data["Name"], data["Average"])
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Pie Chart
subjects = ["Math", "Science", "English"]
avg_marks = data[subjects].mean()

plt.figure()
plt.pie(avg_marks, labels=subjects, autopct='%1.1f%%')
plt.title("Subject Distribution")
plt.show()

# 3. Scatter Plot
plt.figure()
plt.scatter(data["StudyHours"], data["Average"])
plt.title("Study Hours vs Average Marks")
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.show()