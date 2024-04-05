
class Solution(object):
   def twoSumLessThanK(self, A, K):
      result = -1
      if len(A)==1:
         return -1
      for i in range(len(A)):
         for j in range(i+1,len(A)):
            S = A[i] + A[j]
            if S<K:
               result = max(result,S)
      return result
ob1 = Solution()
print(ob1.twoSumLessThanK([34,23,1,24,75,33,54,8],60))
print(ob1.twoSumLessThanK([10, 20, 30],15))