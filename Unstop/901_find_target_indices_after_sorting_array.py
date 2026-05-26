'''
Marco likes numbers a lot. His friend Shyam gives him a number array A  of length N and a target value K. 
He first asks him to sort the array A and to tell him the indices of the numbers where the target value will match with that element.

Help Marco solve this crazy problem and print out the indices of target value K in array A
'''

N=int(input())
A=list(map(int,input().split()))
T=int(input())
B=[]
a=A.sort()
count=0
for i in range(len(A)):
  if A[i]==T:
    count+=1
    B.append(i)

print(count)

print(*B)

#COMPLETE SUBMISSION