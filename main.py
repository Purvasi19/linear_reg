import numpy as np
import matplotlib.pyplot as plt

# Sample data (Hours studied vs Marks)
X = np.array([1, 2, 3, 4, 5])
y = np.array([35, 40, 50, 55, 60])

# Mean of X and y
x_mean = np.mean(X)
y_mean = np.mean(y)

# Calculating slope (m) and intercept (c)
numerator = np.sum((X - x_mean) * (y - y_mean))
denominator = np.sum((X - x_mean) ** 2)

m = numerator / denominator
c = y_mean - m * x_mean

print("Slope (m):", m)
print("Intercept (c):", c)

# Prediction
y_pred = m * X + c

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Linear Regression (From Scratch)")
plt.show()
