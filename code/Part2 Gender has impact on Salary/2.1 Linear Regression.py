import pandas as pd
import numpy as np
import statsmodels.api as sm

# Import data
file_path = "Lawsuit.csv"
data = pd.read_csv(file_path)

# Convert department from nominal to ordinal variable based on average annual salary
dept_avg_sal94 = data.groupby("Dept")["Sal94"].mean().reset_index()
print("Average Salary by Dept in 1994:")
print(dept_avg_sal94)

dept_avg_sal95 = data.groupby("Dept")["Sal95"].mean().reset_index()
print("Average Salary by Dept in 1995:")
print(dept_avg_sal95)

# Adjust department values
data["adjDept"] = data["Dept"].copy()
data.loc[data["Dept"] == 1, "adjDept"] = 2
data.loc[data["Dept"] == 2, "adjDept"] = 1
data.loc[data["Dept"].isin([3, 4, 5, 6]), "adjDept"] = data["Dept"]

# Original multiple linear regression models
X1 = data[["Gender", "Cert", "Exper", "Rank", "adjDept"]]
X1 = sm.add_constant(X1)  # Add intercept
y1 = data["Sal94"]

model_1994 = sm.OLS(y1, X1).fit()
print("Linear Regression Results for 1994:")
print(model_1994.summary())

X2 = data[["Gender", "Cert", "Exper", "Rank", "adjDept"]]
X2 = sm.add_constant(X2)  # Add intercept
y2 = data["Sal95"]

model_1995 = sm.OLS(y2, X2).fit()
print("Linear Regression Results for 1995:")
print(model_1995.summary())

# Moderating variable model: Interaction between gender and department
data["Gender_adjDept"] = data["Gender"] * data["adjDept"]

X3 = data[["Gender", "Gender_adjDept", "adjDept", "Cert", "Exper", "Rank"]]
X3 = sm.add_constant(X3)  # Add intercept
y3 = data["Sal94"]

interaction_model_1994 = sm.OLS(y3, X3).fit()
print("Interaction Model Results for 1994:")
print(interaction_model_1994.summary())

X4 = data[["Gender", "Gender_adjDept", "adjDept", "Cert", "Exper", "Rank"]]
X4 = sm.add_constant(X4)  # Add intercept
y4 = data["Sal95"]

interaction_model_1995 = sm.OLS(y4, X4).fit()
print("Interaction Model Results for 1995:")
print(interaction_model_1995.summary())
