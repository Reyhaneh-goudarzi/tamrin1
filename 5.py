# Get the number of rows (n) from the user
n = int(input("Enter the number of rows (n): "))

# Loop to print the pattern
for i in range(1, n + 1):  # For each row from 1 to n
    for j in range(1, i + 1):  # For each column from 1 to the current row number
        print(i * j, end=' ')  # Print the product of the row and column numbers
    print()  # Move to the next line
