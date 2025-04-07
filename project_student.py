import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
df1 = pd.read_csv("data.csv",usecols=['1st','2nd','3rd','4th','5th'])
row_index = 0
x = df1.columns
y = df1.iloc[row_index]
blue_black_colors = ['b','g','r','m','y']  
plt.bar(x,y,edgecolor="k",color=blue_black_colors)
plt.title("CGPA Trend Across Semesters")
plt.xlabel("Semester",fontsize=15)
plt.ylabel("CGPA",fontsize=15)
plt.show()
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=30,shadow=True,)
plt.title("CGPA Contribution by Semester")
plt.show()
