#Credit Card Fraud Detection

## 📌 Project Overview

Credit Card Fraud Detection is a Machine Learning project that identifies whether a credit card transaction is legitimate or fraudulent.

This project uses the **Random Forest Classifier** algorithm to classify transactions based on transaction details.

Users can enter transaction information and receive a prediction.

## 🎯 Project Objectives

- Detect fraudulent credit card transactions.
- Identify legitimate transactions.
- Train a Machine Learning classification model.
- Accept transaction details from the user.
- Predict transaction status.
- Visualize transaction data and model performance.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Random Forest Classifier

## 📂 Project Structure

```text
Credit_Card_Fraud_Detection/
│
├── .venv/
│
├── creditcard.csv
│
├── fraud_detection.py
│
└── README.md
```

## 📊 Dataset Information

The project uses a sample credit card transaction dataset.

| Column | Description |
|---|---|
| Time | Transaction time |
| V1–V10 | Anonymized transaction features |
| Amount | Transaction amount |
| Class | Target variable |

### Target Variable

| Class | Meaning |
|---|---|
| 0 | Legitimate transaction |
| 1 | Fraudulent transaction |

**Note:** The current practice dataset contains only 20 illustrative records. It is not the original Kaggle dataset.

## 🤖 Machine Learning Algorithm

### Random Forest Classifier

Random Forest is a supervised Machine Learning algorithm that uses multiple decision trees to make predictions.

It is used in this project to classify transactions into:

- Legitimate
- Fraudulent

## ⚙️ Installation

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Required Libraries

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn
```

## ▶️ How to Run

Run the following command:

```bash
python fraud_detection.py
```

## 💻 Sample Input

```text
Enter transaction time: 10
Enter V1 value: -2.31
Enter V2 value: 1.76
Enter V3 value: -0.35
Enter V4 value: 2.33
Enter V5 value: -0.82
Enter V6 value: 0.80
Enter V7 value: 0.73
Enter V8 value: -0.21
Enter V9 value: -0.17
Enter V10 value: 0.48
Enter transaction amount: 0
```

## 📈 Sample Output

```text
===== CREDIT CARD FRAUD DETECTION =====

===== PREDICTION RESULT =====

Transaction Amount: ₹ 0.0
Transaction Status: FRAUDULENT

===== PREDICTION MEANING =====

LEGITIMATE  : Normal transaction
FRAUDULENT  : Suspicious transaction
```

*The prediction above is an illustrative training-example test, not a guaranteed result for every run or a real-world fraud assessment.*

## 📊 Visualizations

The project displays:

1. Legitimate vs Fraudulent Transaction Count.
2. Confusion Matrix.

## 📚 Learning Outcomes

- Understanding supervised Machine Learning.
- Working with classification algorithms.
- Loading and processing CSV datasets.
- Splitting training and testing data.
- Feature scaling using StandardScaler.
- Training a Random Forest model.
- Making predictions using user input.
- Evaluating model performance.
- Creating visualizations using Matplotlib and Seaborn.

## ⚠️ Limitations

- The practice dataset contains only 20 records.
- The dataset contains only V1–V10 instead of all 28 anonymized features.
- Model accuracy is not reliable with this small dataset.
- Predictions are for educational purposes only.
- Real fraud detection requires a much larger and representative dataset.

## 👨‍💻 Author

Tamil

## 📌 Project Status

Completed – Basic Learning Project
