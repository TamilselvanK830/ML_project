
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("salary_data.csv")

X = data[["Experience"]]
y = data["Salary"]

model = LinearRegression()

model.fit(X, y)

experience = float(
    input("\nEnter years of experience: ")
)

prediction = model.predict(
    pd.DataFrame({"Experience": [experience]})
)

print("\n===== SALARY PREDICTION =====")
print("Experience:", experience, "years")
print("Predicted Salary: ₹", round(prediction[0], 2))
