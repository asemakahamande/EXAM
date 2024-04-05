# largest sum of two numbers less than K
A= [34, 23, 1, 24, 75, 33, 54, 8]
K= 60
for i in range(max(A)):
    for j in range(max(A)):
        if A[i]!=A[j]:
            if A[i] + A[j] < K:
                print([A[i], A[j]])
# Given an array A of integers and integer K,
# return the maximum S such that there exist i<j with
# A[i] + A[j] = S and S < K. if no such i, j
# exist satisfying this equation return -1 in python.