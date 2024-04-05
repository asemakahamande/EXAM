#The program inputs the digits and the num. Then using the digits the dictionary is created where the key is the number and the value is its index position. Then the num is iterated over and the target index is
# found out and the amount of distance to be moved is computed.

#Explanation:

#Python code

#take the inputs

digits=input("digits=0123456789")

num=input("num =210")

#create a dictionary to set the digit and index

digitDict={0:0, 1:1, 2:2,3:3,4:4, 5:5, 6:6, 7:7, 8:8, 9:9

}

for i in range(len(digits)):

   digitDict[digits[i]]=i

ans=0

index=0

for digit in num:

   targetIndex=digitDict[digit]

   ans+=abs(index-targetIndex)

   index=targetIndex

print(ans)


