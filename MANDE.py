class Solution:
   def solve(self, nums, k):
      temp_set=set()
      for num in nums:
         if num in temp_set:
            return True
            temp_set.add(k-num)
      return False
ob = Solution()
nums = [45, 18, 9, 13, 12]

k = 31
print(ob.solve(nums, k))

arr=[3,5,7,10]
k=17
flag=False
hashset = set()
for i in range(0,len(arr)):
    if k-arr[i] in hashset:
      flag=True
    hashset.add(arr[i])
print( flag )