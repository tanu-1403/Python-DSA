'''
You are given a row of boxes. Each box can be either "a" or "b".
To check if it's an 'ab' pattern, you need to make sure that all the "a" boxes, if they exist, come before any "b" boxes, if they exist.
If this order is maintained, it's an ab pattern; otherwise, it's not. Display "YES" if it is maintained else "NO". 
'''

s = input().strip()
flag=False
for i in s:
    if i=="a":
        flag==True
    elif i=="b" and not flag:
        print("NO")
    else:
        print("YES")

#INCOMPLETE SUBMISSION 33/100