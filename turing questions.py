#if __name__== '__name__':
 #   conponents = line.strip().split()
  #  A = [34, 23, 1, 24, 75, 33, 54, 8]
   # K = 60
    #for i in A:
     #   A.append(in(A))
    #K = int(input(34, 23, 1, 24, 75, 33, 54, 8), K=60)
    #print(twosumlessthanK(A, K))
     #   def twosumlessthanK(A, K: int) -> int:


#a = [1, 5, 11, 5]
#k=16
#def check_sum(nums, k):
 #   for i in range(len(nums)):
  #      for j in range(i+1, len(nums)):
   #         if nums[i] + nums[j] < k:
    #            return len(nums)
    #return False
#print(check_sum([12, 5, 0, 5], 10))
#print(check_sum([20, 20, 4, 5], 40))
#print(check_sum([1, -1], 0))
#print(check_sum([1, 1, 0], 0))

#58
A = [34, 23, 1, 24, 75, 33, 54, 8]
K=60
def TwoSumLessThanK(num, K):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] < K:
                return TwoSumLessThanK()
            else:
                if nums[i] + nums[j]==0:
                  return -1
print(TwoSumLessThanK(34, 6), 60)