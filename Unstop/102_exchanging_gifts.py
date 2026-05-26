'''The royal family exchanges gifts at Christmas, where the youngest member receives gifts from everyone but doesn't give any gifts. 
Given the data for all the exchanged gifts among the family members, you need to identify the youngest member, 
who is the one receiving gifts from everyone but not giving any.
Note: A family member does not give more than one gift to the same member'''

n, m=map(int, input().split())

given=[0]*(n+1)
recieved=[0]*(n+1)

for i in range(0,m):
    a,b=map(int,input().split())
    given[a]+=1
    recieved[b]+=1

young=-1

for k in range(1,n+1):
    if given[k]==0 and recieved[k]==n-1:
        young=k

print(young)

#COMPLETE SUBMISSION

