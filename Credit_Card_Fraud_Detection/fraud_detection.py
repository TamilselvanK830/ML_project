
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# ===== STEP 1: LOAD DATASET =====

data = pd.read_csv("creditcard.csv")

X = data.drop("Class", axis=1)
y = data["Class"]

# ===== STEP 2: SPLIT DATA =====

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# ===== STEP 3: SCALE DATA =====

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ===== STEP 4: TRAIN MODEL =====

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train_scaled, y_train)

# ===== STEP 5: EVALUATION =====

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

# ===== STEP 6: USER INPUT =====

print("\n===== CREDIT CARD FRAUD DETECTION =====")

time = float(input("Enter transaction time: "))

values = []

for i in range(1, 11):
    values.append(float(input(f"Enter V{i} value: ")))

amount = float(input("Enter transaction amount: "))

# Prepare transaction
new_transaction = pd.DataFrame(
    [[time] + values + [amount]],
    columns=X.columns
)

# ===== STEP 7: PREDICTION =====

new_scaled = scaler.transform(new_transaction)
prediction = model.predict(new_scaled)

print("\n===== PREDICTION RESULT =====")
print("Transaction Amount: ₹", amount)

if prediction[0] == 1:
    print("Transaction Status: FRAUDULENT")
else:
    print("Transaction Status: LEGITIMATE")

print("\n===== PREDICTION MEANING =====")
print("LEGITIMATE  : Normal transaction")
print("FRAUDULENT  : Suspicious transaction")

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# ===== STEP 8: VISUALIZATION =====

plt.figure(figsize=(8, 5))

sns.countplot(x="Class", data=data)

plt.title("Legitimate vs Fraudulent Transactions")
plt.xlabel("0 = Legitimate | 1 = Fraudulent")
plt.ylabel("Number of Transactions")
plt.show()

# ===== STEP 9: CONFUSION MATRIX =====

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Legitimate", "Fraudulent"],
    yticklabels=["Legitimate", "Fraudulent"]
)

plt.title("Credit Card Fraud Detection")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
