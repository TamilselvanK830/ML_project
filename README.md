# House Price Prediction using Machine Learning

## Project Overview
This project uses **Linear Regression**, a supervised machine learning algorithm, to predict house prices based on house size (square feet).

The model is trained using sample house size and price data. Users can enter a new house size, and the trained model predicts its estimated price in lakhs.

## Technologies Used
- Python 3
- NumPy
- Scikit-learn
- Linear Regression
- VS Code
- Git and GitHub

## Project Structure

```text
ML_project1/
│
├── ML1.py
├── README.md
└── .venv/
```

## Dataset

The project uses the following sample training data:

| House Size (sq.ft) | Price (Lakhs) |
|---:|---:|
| 500 | 25 |
| 800 | 40 |
| 1000 | 50 |
| 1200 | 60 |
| 1500 | 75 |

## Machine Learning Algorithm

**Linear Regression**

Linear Regression learns the relationship between house size and house price.

The model uses the training data to learn a relationship and predict prices for new house sizes.

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/TamilselvanK830/ML_project.git
```

### Step 2: Navigate to the project folder

```bash
cd ML_project
```

### Step 3: Create a virtual environment

```bash
python -m venv .venv
```

### Step 4: Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5: Install required libraries

```bash
python -m pip install numpy scikit-learn
```

## How to Run

Execute the Python file:

```bash
python ML1.py
```

Enter the house size when prompted.

## Example Output

```text
Enter House Size (sq.ft): 1100

House Size: 1100.0 sq.ft
Predicted Price: 55.0 Lakhs
```

## Project Workflow

1. Import NumPy and Linear Regression.
2. Prepare training data.
3. Create the Linear Regression model.
4. Train the model using `model.fit()`.
5. Get house size from user input.
6. Predict the house price using `model.predict()`.
7. Display the predicted price.

## Learning Outcomes

- Understanding supervised machine learning.
- Working with NumPy arrays.
- Understanding Linear Regression.
- Training a machine learning model.
- Accepting user input in Python.
- Making predictions using Scikit-learn.

## Future Improvements

- Use a real-world house price dataset.
- Add more features such as location, bedrooms, and age.
- Improve prediction accuracy.
- Build a user-friendly interface.
- Evaluate model performance using appropriate metrics.

## Author

**Tamilselvan K**

GitHub: https://github.com/TamilselvanK830

---

*This is a beginner-friendly Machine Learning project created for learning and practicing Linear Regression.*
