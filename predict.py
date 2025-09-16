with open("model.txt", "r") as f:
    theta0, theta1 = map(float, f.read().split(","))

mileage = float(input("Enter the mileage of the car: "))

with open("data.csv") as file:
    next(file)
    miles = [float(line.strip().split(",")[0]) for line in file]

mileage_scaled = (mileage - min(miles)) / (max(miles) - min(miles))

def estimated_price(x, theta0, theta1):
    return theta0 + theta1 * x

predicted_price = estimated_price(mileage_scaled, theta0, theta1)

print(f"The estimated price for a car with {mileage} miles is: ${predicted_price:.2f}")
