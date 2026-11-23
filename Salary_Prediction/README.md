# Employee Salary Prediction using Machine Learning

## Project Overview
This project predicts an employee's salary based on their years of work experience using Machine Learning.

The project uses the Linear Regression algorithm to train a model with historical salary data and predict salaries for new employees.

## Project Objectives
- Understand the basics of Machine Learning.
- Load and analyze employee salary data.
- Train a Linear Regression model.
- Get experience as user input.
- Predict employee salary.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Linear Regression

## Project Structure

```text
Salary_Prediction/
│
├── salary_prediction.py
├── salary_data.csv
├── README.md
└── .venv/
```

## Dataset
The dataset contains two columns:

| Column | Description |
|---|---|
| Experience | Years of work experience |
| Salary | Employee salary |

## Machine Learning Algorithm
**Linear Regression**

Linear Regression is a supervised Machine Learning algorithm used to predict continuous numerical values.

## How to Run the Project

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Create virtual environment
```bash
python -m venv .venv
```

### 3. Activate environment (Windows PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install libraries
```bash
python -m pip install numpy pandas scikit-learn matplotlib
```

### 5. Run the program
```bash
python salary_prediction.py
```

## Sample Output

```text
Enter years of experience: 6

===== SALARY PREDICTION =====
Experience: 6.0 years
Predicted Salary: ₹45000.0
```

## Learning Outcomes
- Understanding supervised learning.
- Understanding features and target variables.
- Training a Linear Regression model.
- Making predictions using user input.
- Working with Pandas and Scikit-learn.

## Author
Tamil

## Project Status
Beginner Machine Learning Project – In Progress
