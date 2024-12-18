import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Set the working directory and load the lawsuit data
# Note: The path should be updated to the actual path where the 'Lawsuit.csv' file is located
wd = "/Users/xxx"
file_path = 'Lawsuit.csv'
lawsuit_df = pd.read_csv(file_path)

# Summarize the data to check for missing values and drop the ID column
print(lawsuit_df.isnull().sum())
lawsuit_df.drop('ID', axis=1, inplace=True)

# Convert categorical variables to factors with labels
lawsuit_df['Dept'] = pd.Categorical(lawsuit_df['Dept'], categories=range(1, 7), 
                                    ordered=True, 
                                    labels=["Dept 1", "Dept 2", "Dept 3", "Dept 4", "Dept 5", "Dept 6"])
lawsuit_df['Gender'] = pd.Categorical(lawsuit_df['Gender'], categories=[0, 1], 
                                      ordered=True, 
                                      labels=["Female", "Male"])
lawsuit_df['Clin'] = pd.Categorical(lawsuit_df['Clin'], categories=[0, 1], 
                                    ordered=True, 
                                    labels=["Primarily Research", "Primarily Clinical"])
lawsuit_df['Cert'] = pd.Categorical(lawsuit_df['Cert'], categories=[0, 1], 
                                    ordered=True, 
                                    labels=["Not Certified", "Board Certified"])
lawsuit_df['Rank'] = pd.Categorical(lawsuit_df['Rank'], categories=[1, 2, 3], 
                                    ordered=True, 
                                    labels=["Assistant", "Associate", "Full Professor"])
lawsuit_df['SalaryChange'] = lawsuit_df['Sal95'] - lawsuit_df['Sal94']

# Display summary statistics of the dataset
print(lawsuit_df.describe())

# Convert data to long format for plotting
lawsuit_long = pd.melt(lawsuit_df, 
                      id_vars=["Gender", "Dept", "Clin", "Cert", "Prate", "Exper", "Rank"], 
                      measure_vars=["Sal94", "Sal95"],
                      var_name="Year", 
                      value_name="Salary")

# Convert 'Year' to a factor with labels for 1994 and 1995
lawsuit_long['Year'] = pd.Categorical(lawsuit_long['Year'], categories=["Sal94", "Sal95"], 
                                    ordered=True, 
                                    labels=["1994", "1995"])

# Plotting various statistics
# Total Number of Males and Females
plt.figure(figsize=(10, 6))
sns.countplot(x="Gender", data=lawsuit_df, palette=["#0871c2", "#ff689b"])
plt.title("Total Number of Males and Females")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Average Salary Comparison for 1994 and 1995
plt.figure(figsize=(10, 6))
sns.barplot(x="Gender", y="Salary", hue="Gender", data=lawsuit_long, ci=None)
plt.title("Average Salary Comparison for 1994 and 1995")
plt.xlabel("Year")
plt.ylabel("Average Salary")
plt.show()

# Salary Distribution by Gender in 1994 and 1995
plt.figure(figsize=(10, 6))
sns.boxplot(x="Gender", y="Salary", data=lawsuit_long)
plt.title("Salary Distribution by Gender in 1994 and 1995")
plt.xlabel("Gender")
plt.ylabel("Salary")
plt.show()

# Density plot for salary distribution
plt.figure(figsize=(10, 6))
sns.kdeplot(y="Salary", hue="Gender", data=lawsuit_long, palette=["#ff689b", "#0871c2"])
plt.title("Salary Distribution by Gender")
plt.xlabel("Salary")
plt.ylabel("Density")
plt.show()

# Violin plot for salary distribution
plt.figure(figsize=(10, 6))
sns.violinplot(x="Gender", y="Salary", hue="Gender", data=lawsuit_long, palette=["#ff689b", "#0871c2"])
plt.title("Salary Distribution by Gender in 1994 and 1995")
plt.xlabel("Gender")
plt.ylabel("Salary")
plt.show()

# Salary Change in 1994-1995
plt.figure(figsize=(10, 6))
sns.barplot(x="Gender", y="SalaryChange", hue="Gender", data=lawsuit_df, ci=None)
plt.title("Salary Change by Gender in 1994-1995")
plt.xlabel("Gender")
plt.ylabel("Salary Change")
plt.show()

# Rank Distribution by Gender
plt.figure(figsize=(10, 6))
sns.barplot(x="Rank", y="count", hue="Gender", data=lawsuit_df, ci=None)
plt.title("Rank Distribution by Gender")
plt.xlabel("Rank")
plt.ylabel("Count")
plt.show()

# Average Salary by Rank and Gender for 1994 and 1995
plt.figure(figsize=(10, 6))
sns.barplot(x="Rank", y="Salary", hue="Gender", data=lawsuit_long, ci=None)
plt.title("Average Salary by Rank and Gender for 1994 and 1995")
plt.xlabel("Rank")
plt.ylabel("Average Salary")
plt.show()

# Gender Distribution by Department
plt.figure(figsize=(10, 6))
sns.countplot(x="Dept", hue="Gender", data=lawsuit_df, palette=["#0871c2", "#ff689b"])
plt.title("Gender Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

# Calculate average salaries by department for each year and reorder departments
avg_salaries = lawsuit_df.groupby('Dept')[['Sal94', 'Sal95']].mean().reset_index()
ordered_depts = avg_salaries.sort_values(by='Sal95')['Dept']
lawsuit_df['Dept'] = pd.Categorical(lawsuit_df['Dept'], categories=ordered_depts, 
                                    ordered=True, 
                                    labels=["adjDept 1", "adjDept 2", "adjDept 3", "adjDept 4", "adjDept 5", "adjDept 6"])

# Plot for 1995
plt.figure(figsize=(10, 6))
sns.barplot(x="Dept", y="Sal95", data=lawsuit_df, palette="Greys")
plt.title("Average Salary by Department for 1995")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# Plot for 1994
plt.figure(figsize=(10, 6))
sns.barplot(x="Dept", y="Sal94", data=lawsuit_df, palette="Greys")
plt.title("Average Salary by Department for 1994")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# Plot average salary by department and gender for 1995
plt.figure(figsize=(10, 6))
sns.pointplot(x="Dept", y="Sal95", hue="Gender", data=lawsuit_df, palette=["#ff689b", "#0871c2"])
plt.title("Average Salary by Department and Gender for 1995")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# Plot average salary by department and gender for 1994 and 1995
plt.figure(figsize=(10, 6))
sns.barplot(x="Dept", y="Salary", hue="Gender", data=lawsuit_long, palette=["#ff689b", "#0871c2"])
plt.title("Average Salary by Department and Gender for 1994 and 1995")
plt.xlabel("Rank")
plt.ylabel("Average Salary")
plt.show()

# Plot salary change by rank and gender
plt.figure(figsize=(10, 6))
sns.barplot(x="Rank", y="Sal94", hue="Gender", data=lawsuit_df, palette=["#ff689b", "#0871c2"])
plt.title("Salary Change by Rank and Gender")
plt.xlabel("Rank")
plt.ylabel("Salary")
plt.show()

# Plot publication rate vs salary comparison
plt.figure(figsize=(10, 6))
sns.regplot(x="Prate", y="Salary", hue="Gender", data=lawsuit_long, palette=["#ff689b", "#0871c2"])
plt.title("Publication Rate vs Salary by Gender (1994 & 1995)")
plt.xlabel("Publication Rate")
plt.ylabel("Salary")
plt.show()

# Plot experience vs salary by gender (1994 & 1995)
plt.figure(figsize=(10, 6))
sns.regplot(x="Exper", y="Salary", hue="Gender", data=lawsuit_long, palette=["#ff689b", "#0871c2"])
plt.title("Experience vs Salary by Gender (1994 & 1995)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# Plot experience vs salary by certification and gender
plt.figure(figsize=(10, 6))
sns.regplot(x="Exper", y="Sal94", hue="Gender", data=lawsuit_df, palette=["#ff689b", "#0871c2"])
plt.title("Experience vs Salary by Certification and Gender")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# Plot experience vs salary in 1995 by rank and department
plt.figure(figsize=(10, 6))
sns.regplot(x="Exper", y="Sal95", hue="Gender", data=lawsuit_df, palette=["#ff689b", "#0871c2"])
plt.title("Experience vs Salary in 1995 by Rank and Department")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# Plot publication rate vs salary comparison
plt.figure(figsize=(10, 6))
sns.regplot(x="Prate", y="Salary", hue="Gender", data=lawsuit_long, palette=["#ff689b", "#0871c2"])
plt.title("Publication Rate vs Salary by Gender (1994 & 1995)")
plt.xlabel("Publication Rate")
plt.ylabel("Salary")
plt.show()

