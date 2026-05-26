'''
Given an array of integer, an astrologer has determined that it is not lucky and needs to be changed.
The suggested modification involves increasing the value at each index by the maximum value encountered up to that index. 
Your task is to print the modified array.
'''

n=int(input())
arr=list(map(int,input().split()))
arr1=[]

for j in range(n):
    max1=arr[j]
    max1==max(max1,arr[j])    
    arr1.append(arr[j]+max1)

print(*arr1)

#INCOMPLETE SUBMISSION 42/100