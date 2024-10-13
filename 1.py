# Function to get even digits and separate them by '*'
def print_even_digits(number):
    # Convert the number to a string to iterate over each digit
    number_str = str(number)

    # Initialize an empty list to store even digits
    even_digits = []

    # Iterate over each digit in the number string
    for digit in number_str:
        # Check if the digit is even (and it's not zero)
        if int(digit) % 2 == 0:
            even_digits.append(digit)

    # Join the even digits with '*' separator and print the result
    if even_digits:
        print('*'.join(even_digits))
    else:
        print("No even digits found.")


# Input: number
number = int(input("Enter a number: "))
print_even_digits(number)