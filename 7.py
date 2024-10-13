import math


# Function to find the maximum number
def Max1(numbers):
    return max(numbers)


# Function to find the minimum number
def Min1(numbers):
    return min(numbers)


# Function to calculate average and print it
def Ave1(numbers):
    average = sum(numbers) / len(numbers)
    print(f"Average: {average}")


# Function to calculate standard deviation and print it
def STD1(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    print(f"Standard Deviation: {std_dev}")


# Main function
def main():
    # Get 5 numbers from the user
    numbers = []
    for i in range(5):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Call the functions and display results
    maximum = Max1(numbers)
    minimum = Min1(numbers)

    print(f"\nResults:")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

    Ave1(numbers)  # This function prints the average
    STD1(numbers)  # This function prints the standard deviation


# Run the main function
if __name__ == "__main__":
    main()
