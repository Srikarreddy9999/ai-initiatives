import sklearn.datasets as ds
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

# Load digits dataset
X, y = ds.load_digits(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with standardization and logistic regression
clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))

# Train
clf.fit(X_train, y_train)

# Evaluate
predictions = clf.predict(X_test)
acc = accuracy_score(y_test, predictions)
print(f"Test accuracy: {acc:.2%}")
