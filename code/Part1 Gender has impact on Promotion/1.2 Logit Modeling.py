import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNetCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
lawsuit = pd.read_csv("Lawsuit.csv")

# Remove unnecessary columns and convert categorical variables to factors
lawsuit_new = lawsuit.drop(columns=[0, 8, 9])
lawsuit_new['Dept'] = lawsuit_new['Dept'].astype('category')
lawsuit_new['Gender'] = lawsuit_new['Gender'].astype('category')

# Create a binary rank variable
lawsuit_new['Rank'] = lawsuit_new['Rank'].apply(lambda x: 0 if x in [1, 6] else 1)

# Perform logistic regression
rank = lawsuit_new['Rank']
features = ['Dept', 'Gender', 'Clin', 'Cert', 'Prate', 'Exper']
X = lawsuit_new[features]
y = rank
X = pd.get_dummies(X, drop_first=True)  # Convert categorical variables to dummy/indicator variables
model = pd.concat([X, y], axis=1)  # Combine features with target variable
X_matrix = model.drop('Rank', axis=1)
y_vector = model['Rank']
X_matrix = StandardScaler().fit_transform(X_matrix)  # Standardize the features
model = LogisticRegression(C=1.0, penalty='l2')  # Use L2 penalty for logistic regression
model.fit(X_matrix, y_vector)
print(f"Coefficients: {model.coef_}")
predictions = model.predict_proba(X_matrix)[:, 1]
predicted_class = (predictions > 0.5).astype(int)

# Confusion matrix
print(pd.crosstab(y_vector, predicted_class))

# Elastic Net
without_ID = lawsuit.drop(columns=[0])
y = without_ID['Rank']
X = without_ID.drop(columns=['Rank', 'Dept', 'Gender'])
X = pd.get_dummies(X, drop_first=True)  # Convert categorical variables to dummy/indicator variables
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
elastic_net = ElasticNetCV(l1_ratio=[.1, .5, .7, .9, .95, 1], n_alphas=50, cv=20)
elastic_net.fit(X_scaled, y)
print(f"Best alpha: {elastic_net.alpha_}, Best L1 ratio: {elastic_net.l1_ratio_}")

# ROC Curve
fpr, tpr, thresholds = roc_curve(y, predictions)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()