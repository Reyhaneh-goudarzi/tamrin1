import math

# Function to calculate standard deviation
def calculate_std(numbers, mean):
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

# Get the number of inputs from the user
n = int(input("Enter the number of numbers (n): "))

# Initialize an empty list to store the numbers
numbers = []

# Loop to get n numbers from the user
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate maximum, minimum, and average
maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / n

# Calculate standard deviation
std_dev = calculate_std(numbers, average)

# Print results
print(f"\nResults:")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Average: {average}")
print(f"Standard Deviation: {std_dev}")
