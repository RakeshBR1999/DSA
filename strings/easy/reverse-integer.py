# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1],
#  then return 0.

def reverseinteger(n):
    signn = 1
    if n>0:
        signn=1
    else:
        signn=-1
    n = abs(n)
    reversed_num = 0
    while n>0:
        rem = n%10
        reversed_num = reversed_num*10 + rem
        n = n//10
    reversed_num = signn*reversed_num
    if reversed_num>2**31-1 or reversed_num<-2**31:
        return 0
    return reversed_num


print(reverseinteger(-123))
print(reverseinteger(123))
print(reverseinteger(-156469))
print(reverseinteger(-1534236469))

# Time: O(log(n)) — Number of digits in n
# Space: O(1) — Constant space for variables