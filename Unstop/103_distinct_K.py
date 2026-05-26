'''
You wish to help Ashish, who possesses a collection of N strings, some of which may be duplicated, 
and has been assigned the task of finding the kth unique string.
If the number of unique strings is less than k, he needs to display -1. Considering you are Ashish's 
best friend can you assist him with this challenge?
'''

w=int(input())

l=[]

for i in range(w):
  a=input()
  l.append(a)

k=int(input())

count={}

for j in l:
  if j in count:
    count[j]+=1
  else:
    count[j]=1

result=[]

for key,value in count.items():
  if value==1:
    result.append(key)

if len(result)>=k:
  print(result[k-1])
else:
  print(-1)

#COMPLETE SUBMISSIONS  
