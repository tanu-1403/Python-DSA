'''
Reena has a basket containing an array of 2N fruits.
She needs to pair these fruits into N pairs, (a1, b1) , (a2, b2),.....,(an, bn), such that the sum of the minimum values in each pair, 
min(ai, bi) for all i is maximized.
Your task is to calculate and print this maximum possible sum.
'''

n=int(input())
l1=list(map(int,input().split()))
l1.sort()
a=sum(l1[::2])
print(a)

#COMPLETE SUBMISSION