
import numpy as np
from sklearn.linear_model import LinearRegression

# Step 1: Training data
X = np.array([[500], [800], [1000], [1200], [1500]])

# Step 2: Correct answers
y = np.array([25, 40, 50, 60, 75])

# Step 3: Create Machine Learning model
model = LinearRegression()

# Step 4: Train the model
model.fit(X, y)

# Step 5: Get user input
house_size = float(input("Enter House Size (sq.ft): "))

# Step 6: Predict price
new_house = [[house_size]]
prediction = model.predict(new_house)

# Step 7: Display result
print("House Size:", house_size, "sq.ft")
print("Predicted Price:", round(prediction[0], 2), "Lakhs")
