#if __name__=='__main__':
 #   line = input()
  #  A=line.strip().split()
   # A = [34,23,1,24,75,33,54,8]
#K=60
#Given a list of numbers and a number k, write a Python program to check whether the sum of any two numbers from the list is equal to k or not.
# For example, given [1, 5, 11, 5] and k = 16, return true since 11 + 5 is 16.

#Sample Solution:

#Python Code:
a = [1, 5, 11, 5]
k=16
def check_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False
print(check_sum([12, 5, 0, 5], 10))
print(check_sum([20, 20, 4, 5], 40))
print(check_sum([1, -1], 0))
print(check_sum([1, 1, 0], 0))


for i, item in enumerate(numbers):
    for j in range(i+1, len(numbers)):
        total_of_two_items = numbers[i] + numbers[j]
        if(total_of_two_items == total_number):
            print('{first_item} {second_item}'.format(first_item=i+1, second_item=j+1))
