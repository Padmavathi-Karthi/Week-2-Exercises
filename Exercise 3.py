# The function accepts two numeric variables through the function parameters and divides the “numerator” by the “denominator”. The function’s main purpose is to prevent a ZeroDivisionError by checking if the “denominator” is 0. If it is 0, the function should return 0 instead of attempting the division. Otherwise all other numbers will be part of the division equation. Complete the body of the function so that the function completes its purpose. 

def safe_division(numerator, denominator):
    # Complete the if block to catch any "denominator" variables
    # that are equal to 0.
    if denominator==0:
        result = 0
    else:
        # Complete the division equation.
        result = numerator/denominator
    return result


print(safe_division(5, 5)) # Should print 1.0
print(safe_division(5, 4)) # Should print 1.25
print(safe_division(5, 0)) # Should print 0
print(safe_division(0, 5)) # Should print 0.0