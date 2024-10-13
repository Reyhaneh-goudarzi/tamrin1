# Function to check if the sum of the first two digits equals the product of the last two digits
def check_number(num):
    # Convert the number into a string to easily access individual digits
    str_num = str(num)

    # Extract the digits
    d1 = int(str_num[0])  # First digit
    d2 = int(str_num[1])  # Second digit
    d3 = int(str_num[2])  # Third digit
    d4 = int(str_num[3])  # Fourth digit

    # Check if the sum of first two digits equals the product of the last two digits
    if d1 + d2 == d3 * d4:
        return True
    else:
        return False


# Iterate through all 4-digit numbers from 1000 to 9999
for num in range(1000, 10000):
    if check_number(num):
        print(num)
