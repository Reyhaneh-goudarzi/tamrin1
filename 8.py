def F1(number):
    # Find and return the maximum digit in the number
    return max(int(digit) for digit in number)


def F2(max_digit, number):
    # Remove the first occurrence of the maximum digit from the number
    return number.replace(str(max_digit), '', 1)  # Replace only the first occurrence


def main():
    while True:
        number = input("Enter a 5-digit number: ")

        # Check if the number is a 5-digit number
        if len(number) == 5 and number.isdigit():
            break  # Exit loop if a valid number is entered
        else:
            print("Invalid input. Please enter a valid 5-digit number.")

    # Find the maximum digit
    max_digit = F1(number)

    # Remove the maximum digit from the number
    final_number = F2(max_digit, number)

    # Print the final output
    print(f"The maximum digit is: {max_digit}")
    print(f"The number after deleting the maximum digit: {final_number}")


# Run the main function
if __name__ == "__main__":
    main()
