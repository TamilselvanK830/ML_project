
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ===== STEP 1: LOAD CUSTOMER DATA =====

data = pd.read_csv("customer_data.csv")

print("===== CUSTOMER DATA =====")
print(data.head())

# ===== STEP 2: SELECT FEATURES =====

X = data[["Annual_Income", "Spending_Score"]]

# ===== STEP 3: SCALE DATA =====

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ===== STEP 4: APPLY K-MEANS =====

model = KMeans(n_clusters=3, random_state=42, n_init=10)

model.fit(X_scaled)

data["Cluster"] = model.labels_

# ===== STEP 5: DISPLAY CUSTOMER SEGMENTS =====

print("\n===== CUSTOMER SEGMENTS =====")
print(data)

print("\n===== CLUSTER COUNTS =====")
print(data["Cluster"].value_counts().sort_index())

# ===== STEP 6: GET USER INPUT =====

print("\n===== CUSTOMER SEGMENTATION =====")

income = float(input("Enter annual income: "))
spending = float(input("Enter spending score (0-100): "))

if income <= 0 or spending < 0 or spending > 100:

    print("\nInvalid input! Please enter valid values.")

else:

    # Prepare new customer data
    new_customer = pd.DataFrame({
        "Annual_Income": [income],
        "Spending_Score": [spending]
    })

    # Scale new customer data
    new_customer_scaled = scaler.transform(new_customer)

    # Predict customer cluster
    cluster = model.predict(new_customer_scaled)

    print("\n===== PREDICTION RESULT =====")
    print("\nAnnual Income:", income)
    print("Spending Score:", spending)
    print("Customer belongs to Cluster:", cluster[0])

    # ===== STEP 7: VISUALIZATION =====

    plt.figure(figsize=(10, 6))

    # Display existing customer clusters
    for cluster_id in sorted(data["Cluster"].unique()):

        cluster_data = data[data["Cluster"] == cluster_id]

        plt.scatter(
            cluster_data["Annual_Income"],
            cluster_data["Spending_Score"],
            s=100,
            label=f"Cluster {cluster_id}"
        )

    # Highlight new customer
    plt.scatter(
        income,
        spending,
        color="red",
        marker="*",
        s=300,
        edgecolors="black",
        label="New Customer"
    )

    # Add labels
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")

    plt.title("Customer Segmentation using K-Means")

    plt.legend()
    plt.grid(True)

    plt.show()
