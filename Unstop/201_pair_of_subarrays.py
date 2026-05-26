'''
You are given an array A of size N.
Your task is to count the number of unique pairs of non-overlapping subarrays such that both subarrays have the same sum.
Each subarray is defined by a pair of indices [L, R] (1-based indexing), where 1 ≤ L ≤ R ≤ N.
Two subarrays must not overlap, meaning they should not share any common index.
Also, the pair ([L1, R1], [L2, R2]) is considered the same as ([L2, R2], [L1, R1]), so count each valid pair only once.
'''

def calculate_pairs(n, arr):
    prefix=[0]*(n+1)
    for i in range(n):
        prefix[i+1]=prefix[i]+arr[i]
            
    a=0
    for k in range(n):
        for l in range(k,n):
            s=prefix[l+1]-prefix[k]

            for k1 in range(l+1, n):
                for l1 in range(k1, n):
                    if prefix[l1+1]-prefix[k1]==s:
                        a+=1                   
    return a

    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])  # The first line of input, integer N
    arr = list(map(int, data[1:n+1]))  # The second line of input, N space-separated integers
    result = calculate_pairs(n, arr)
    print(result)

if __name__ == "__main__":
    main()

#INCOMPLETE SUBMISSION 83/100