import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from scipy.stats import norm

# Load data
data = pd.read_csv("Lawsuit.csv")  # Replace with your data file path

# Preprocess data
data['Promotion'] = [1 if rank > 2 else 0 for rank in data.Rank]
X = data[['Gender', 'Exper']]  # Feature matrix
y = data['Promotion']  # Target variable

# Encode categorical variables (if needed)
X = pd.get_dummies(X, columns=['Gender'])

# Create and train logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Create new data points for prediction
exper_range = np.linspace(0, 50, 100)  # Assume experience range is from 0 to 50 years

X_male = pd.DataFrame({'Exper': exper_range, 'Gender_0': np.zeros(len(exper_range)), 'Gender_1': np.ones(len(exper_range))})
X_female = pd.DataFrame({'Exper': exper_range, 'Gender_0': np.ones(len(exper_range)), 'Gender_1': np.zeros(len(exper_range))})

# Predict probabilities
probabilities_m = model.predict_proba(X_male)[:, 1]
probabilities_f = model.predict_proba(X_female)[:, 1]

# Calculate confidence intervals
ci_m = norm.ppf(0.975) * np.sqrt(probabilities_m * (1 - probabilities_m) / len(exper_range))
ci_f = norm.ppf(0.975) * np.sqrt(probabilities_f * (1 - probabilities_f) / len(exper_range))

# Plot results
plt.plot(exper_range, probabilities_m, label='Male Probability',color='#0871c2')
plt.plot(exper_range, probabilities_f, label='Female Probability',color='#ff689b')

plt.fill_between(exper_range, probabilities_m - ci_m, probabilities_m + ci_m, alpha=0.2, label='Male CI',color='#0871c2')
plt.fill_between(exper_range, probabilities_f - ci_f, probabilities_f + ci_f, alpha=0.2, label='Female CI',color='#ff689b')

plt.title('Effect of Experience on Promotion Probability by Gender')
plt.xlabel('Years of Experience')
plt.ylabel('Probability')
plt.legend()
plt.grid(True)
plt.show()