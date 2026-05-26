'''
Rahul has an integer array called 'arr' of length N containing unique values. He wants to create a balanced tree 
where each parent node has smaller valued nodes on its left and larger valued nodes on its right. 
This balanced tree should ensure that the depth of the two subtrees for every node doesn't differ by more than one.

Your task is to assist him in creating this type of tree.

The output contains N lines denoting the pre-order traversal of nodes. If the left child of the node contains not 
null value then print the value else print a dot(.) , a similar process for the right child also. Each right child value is 
separated from the node by “->” sign and each left child by a left arrow sign

'''

'''N = int(input())
arr = list(map(int, input().split()))
arr.sort()
left_node=[]
right_node=[]
root=arr[N//2]
arr.remove(root)
for i in arr:
  if root>i:
    left_node.append(i)
  else:
    right_node.append(i)
'''

# Read input
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

# Use a stack to simulate recursion (pre-order)
# Each element in the stack: (subarray)
stack = [arr]

while stack:
    current = stack.pop()
    if not current:
        continue

    mid = len(current) // 2
    root = current[mid]

    # Left and right subarrays
    left_sub = current[:mid]
    right_sub = current[mid+1:]

    # Determine left and right values
    left_val = left_sub[len(left_sub)//2] if left_sub else "."
    right_val = right_sub[len(right_sub)//2] if right_sub else "."
    

    # Print in the required format
    print(f"{left_val} <- {root} -> {right_val}")

    # Push right first so left subtree is processed first
    if right_sub:
        stack.append(right_sub)
    if left_sub:
        stack.append(left_sub)

#COMPLETE SUBISSION