'''
Kritika has a collection of 2*n boxes, with n unique labels. Among them, one box is repeated n times.
How can Kritika identify and print the label of the repeated box?
'''

boxes = int(input())          # this is 2*n
arr = list(map(int, input().split()))

n = boxes // 2                # actual repetition count

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count == n:
        print(arr[i])
        break

#INCOMPLETE SUBMISSION 82/100