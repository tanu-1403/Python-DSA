'''
Steve is participating in competitive coding.

Whenever he makes a submission at time 't', any submission made exactly 5000 seconds before 't' is removed from the queue.
Given N submissions, where each submission is associated with a distinct time 't', determine the maximum size of the 
submission queue at any point in time after all 'N submissions.

Note: It is guaranteed that every submission uses a strictly larger value of ‘t’ than the previous submission.
'''

n=int(input())
l1=list(map(int,input().split()))

a=0
count=0

for i in range(n):
  while l1[i]-l1[a]>=5000:
    a+=1
  count=max(count,i-a+1)

print(count)

#COMPLETE SUBMISSION