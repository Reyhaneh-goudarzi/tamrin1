import math

def compute_expression(num_terms):
    total = 0
    sign = 1  # Alternates between +1 and -1 for addition and subtraction
    odd_num = 3
    numerator_val = 2
    denominator_val = 9

    for i in range(num_terms):
        # Compute factorial for the numerator (odd number factorial)
        factorial = math.factorial(odd_num)

        # Compute denominator (varies according to the pattern)
        denominator = numerator_val + denominator_val

        # Update the total based on the current term
        total += sign * (factorial / denominator)

        # Alternate the sign for the next term
        sign *= -1

        # Increment odd number for factorial by 2 (to get the next odd number)
        odd_num += 2

        # Update numerator and denominator for the next term
        numerator_val += 1
        denominator_val -= 1

        # If the denominator term becomes negative, switch to positive addition
        if denominator_val < 0:
            denominator_val = abs(denominator_val)

    return total

# Compute the result for 500 terms
num_terms = 500
result = compute_expression(num_terms)

# Print the result
print(f"The result of the expression for {num_terms} terms is: {result}")


"""این کد با پیغام خطا OverflowError: integer division result too large for a float مواجه است 
این خطا معمولا به دلیل مقادیر فاکتوریل بسیار بزرگ یا بسیار کوچک ایجاد میشود
"""
