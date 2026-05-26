'''
You have an array of size N, and your task is to count the number of pairs (A[i], A[j]) where i < j.

For each pair, you need to check if the bitwise XOR of A[i] and A[j] is less than or equal to the bitwise 
AND of A[i] and A[j]. In other words, find how many pairs satisfy the condition A[i]⊕A[j] <= A[i]&A[j].
'''

from collections import defaultdict

def msb(x):
    return x.bit_length() - 1

N=int(input())
arr=list(map(int,input().split()))

groups = defaultdict(list)
for x in arr:
    groups[msb(x)].append(x)

count=0

for group in groups.values():
    m=len(group)
    for i in range(m):
        for j in range(i+1,m):
            if (group[i]^group[j] <= group[i]&group[j]):
                count+=1

print(count)

#COMPLETE SUBMISSION