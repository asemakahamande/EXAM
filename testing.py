def count_num_finger(n):
    r = n % 8
    if r == 0:
        return 2
    if r < 5:
        return r
    else:
        return 10 - r
# Driver Code
n = 30
print(count_num_finger(n))

# This code is contributed by "Sharad_Bhardwaj".
def count_num_finger(n):
    r = n % 8
    if r == 0:
        return 2
    if r < 5:
        return r
    else:
        return 10 - r


# Driver Code
n = 30
print(count_num_finger(n))

# This code is contributed by "Sharad_Bhardwaj".

def count_fingers(n):
    # calculate the number of full hands
    full_hands = n // 10

    # calculate the number of fingers used in full hands
    full_fingers = full_hands * 10

    # calculate the number of remaining fingers
    remaining_fingers = n % 10

    # calculate the total number of fingers used
    total_fingers = full_fingers + remaining_fingers

    # return the total number of fingers used
    return total_fingers


# example usage
n = 23
total_fingers = count_fingers(n)
print("Total number of fingers used to count", n, "is", total_fingers)