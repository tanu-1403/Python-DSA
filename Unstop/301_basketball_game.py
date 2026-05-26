'''
In a peculiar basketball game, where World Cup is happening, Aniket is tasked with keeping the scores of the match. 
The game unfolds in rounds, and with each rounds there is a system like the matches played previously will be highlighted 
in future scores too i.e where the scores of previous rounds can influence those in the future.

Aniket starts each game with an null record.
He is provided with a list of operations, represented by strings, denoted as 'ops'.
Each operation, 'ops[i]', can be one of the following:

An integer 'x', indicating the recording of a new score 'x'.
A '+', which means recording a score that is the sum of the previous two scores (it is ensured that there are always at least two previous scores available).
A 'D', signifying recording a score that is double the previous score (it is ensured that there is always a previous score available).
A 'C', indicating the invalidation of the previous score, removing it from the record (it is ensured that there is always a previous score to remove).
Aniket's task is to process these operations and calculate the sum of all the scores and keep record of it for the final judgement.
'''

n = int(input()) 
ops = input().split() 
a=[] 
for o in ops:
    o=o.strip() 
    if o=="C": 
        a.pop() 
    elif o=="+": 
        a.append(a[-2]+a[-1]) 
    elif o=="D": 
        a.append(2*a[-1]) 
    else: 
        a.append(int(o)) 
                        
print(sum(a))

#COMPLETE SUBMISSION