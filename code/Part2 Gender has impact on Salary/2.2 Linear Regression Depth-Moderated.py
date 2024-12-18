import pandas as pd
from statsmodels.formula.api import ols

# Set the working directory and load the lawsuit data
wd = "D:/xxx"
lawsuit = pd.read_csv("Lawsuit.csv")

# Convert department from nominal variable to ordinal variable based on the annual average salary
lawsuit['adjDept'] = lawsuit['Dept']
lawsuit.loc[lawsuit['Dept'] == 1, 'adjDept'] = 2
lawsuit.loc[lawsuit['Dept'] == 2, 'adjDept'] = 1
lawsuit.loc[(lawsuit['Dept'] == 3) | (lawsuit['Dept'] == 4) | (lawsuit['Dept'] == 5) | (lawsuit['Dept'] == 6), 'adjDept'] = lawsuit['Dept']

# Build the original multiple linear regression for Sal94
pmodel = ols('Sal94 ~ Gender + Cert + Exper + Rank + adjDept', data=lawsuit).fit()
print(pmodel.summary())

# Build the original multiple linear regression for Sal95
model = ols('Sal95 ~ Gender + Cert + Exper + Rank + adjDept', data=lawsuit).fit()
print(model.summary())

# Build the moderating variable model to investigate how department plays a role in the relationship between gender and salary for Sal94
pmodel1 = ols('Sal94 ~ Gender + Gender:adjDept + adjDept + Cert + Exper + Rank', data=lawsuit).fit()
print(pmodel1.summary())

# Build the moderating variable model to investigate how department plays a role in the relationship between gender and salary for Sal95
model1 = ols('Sal95 ~ Gender + Gender:adjDept + adjDept + Cert + Exper + Rank', data=lawsuit).fit()
print(model1.summary())