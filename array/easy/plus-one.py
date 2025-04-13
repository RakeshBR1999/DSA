# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.
def plusone(digits):
    l = ""
    for i in digits:
        l = l +str(i)
    l = int(l) + 1
    l = str(l)
    result = [int(i) for i in l]

    return result


# Example usage:    
digits = [1,2,3]
print(plusone(digits)) # Output: [1,2,4]
digits = [9,9,9]
print(plusone(digits)) # Output: [1,0,0,0]