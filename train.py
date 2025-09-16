X = []
Y = []

with open("data.csv") as file:
    next(file)
    for line in file:
        mil, price = line.strip().split(",")
        X.append(float(mil))
        Y.append(float(price))

X_scaled = [(x - min(X)) / (max(X) - min(X)) for x in X]

def estimated_price(x, theta0, theta1):
    return theta0 + theta1 * x

theta0 = 0
theta1 = 0  

alpha = 0.01
num_iterations = 1000

for i in range(num_iterations):
    sum_error_theta0 = 0
    sum_error_theta1 = 0

    for j in range(len(X_scaled)):
        prediction = estimated_price(X_scaled[j], theta0, theta1)
        error = prediction - Y[j]
        sum_error_theta0 += error
        sum_error_theta1 += error * X_scaled[j]

    theta0 = theta0 - alpha * (sum_error_theta0 / len(X_scaled))
    theta1 = theta1 - alpha * (sum_error_theta1 / len(X_scaled))


with open("model.txt", "w") as f:
    f.write(f"{theta0},{theta1}")

print("Training complete! Thetas saved to model.txt")
