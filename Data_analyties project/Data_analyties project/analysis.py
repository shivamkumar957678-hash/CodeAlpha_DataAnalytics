import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data
data = pd.read_csv("data.csv")

# Step 2: Basic info
print("First 5 rows:")
print(data.head())

print("\nData Info:")
print(data.info())

print("\nSummary:")
print(data.describe())

# Step 3: Average marks
data["Average"] = (data["Math"] + data["Science"] + data["English"]) / 3

print("\nAverage Marks:")
print(data[["Name", "Average"]])

# Step 4: Gender-wise average
gender_avg = data.groupby("Gender")["Average"].mean()
print("\nGender-wise Average:")
print(gender_avg)

# Step 5: Plot graph
plt.bar(data["Name"], data["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance")
plt.show()