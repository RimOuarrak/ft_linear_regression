X = []
Y = []


with open("data.csv") as file:
    next(file)
    for line in file:
        mil, price = line.strip().split(",")
        X.append(float(mil))
        Y.append(float(price))


print("First 5 rows:")
for i in range(5):
    print(f"Mileage= {X[i]}, Price={Y[i]}")

print(f"\nNumber of rows: {len(X)}")

print(f"Mileage -> min: {min(X)}, max: {max(X)}, mean: {sum(X)/len(X)}")
print(f"Price -> min: {min(Y)}, max: {max(Y)}, mean: {sum(Y)/len(Y)}")

X_scaled = [(x - min(X)) / (max(X) - min(X)) for x in X]

for i in range(5):
    print(f"scaled= {X_scaled[i]}")

def estimated_price(x, theta0, theta1):
    return theta0 + theta1 * x

theta0 = 0
theta1 = 0  

x1 = X_scaled[0]
x2 = X_scaled[1]
x3 = X_scaled[2]
x4 = X_scaled[3]
x5 = X_scaled[4]

# print(estimated_price(x1, theta0, theta1))
# print(estimated_price(x2, theta0, theta1))
# print(estimated_price(x3, theta0, theta1))
# print(estimated_price(x4, theta0, theta1))
# print(estimated_price(x5, theta0, theta1))


def cost_function(X_scaled,Y, theta0, theta1):
    sum = 0
    s = len(Y)
    for i in range(s):
        prediction = estimated_price(X_scaled[i], theta0, theta1)
        error = prediction - Y[i]
        cost = error ** 2
        sum += cost
    return sum / (2 * s)


# print(f"this: {cost_function(X_scaled, Y, theta0, theta1)}")
num_iterations = 1000
predictions = []


alpha = 0.01
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

    # if (i + 1) % 100 == 0:
    #     print(f"Iteration {i+1}, theta0={theta0}, theta1={theta1}")

mileage = float(input("Enter the mileage of the car: "))
mileage_scaled = (mileage - min(X)) / (max(X) - min(X))
predicted_price = estimated_price(mileage_scaled, theta0, theta1)
print(f"The estimated price for a car with {mileage} miles is: ${predicted_price:.2f}")

