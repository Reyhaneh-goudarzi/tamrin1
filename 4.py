# Function to check if all digits of the number are even
def has_all_even_digits(num):
    # Convert the number to a string to access individual digits
    str_num = str(num)

    # Check each digit to see if it's even
    for digit in str_num:
        if int(digit) % 2 != 0:  # If the digit is odd, return False
            return False
    return True


# Loop through all 3-digit numbers from 100 to 999
for num in range(100, 1000):
    if has_all_even_digits(num):
        print(num)
