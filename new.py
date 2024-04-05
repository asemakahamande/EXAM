# question 2 answer coding challenge
def typing_time(digits, num):
    typing_time = 0
    start = 0
    for digit in num:
        index = digits.index(digit)
        typing_time += abs(start - index)
        start = index
    return typing_time

# Test code
print(typing_time('0123456789', '210'))
print(typing_time('8459761203', '5439'))