'''
Robert wants to organize a marathon across your city.
The city has landmarks numbered from to that can act as starting or finishing points. 
The landmarks are connected by roads. Each road has a length of n. The city map resembles a binary tree in which each 
landmark represents a vertex of the tree, and each road represents an edge. The tree is rooted at vertex 1.

As the first step in planning, he wants to find the longest simple path between any two landmarks in the city.
Help Robert to find the maximum length of the marathon he can organize.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def user_logic(root):
    
    """
    Write your logic here to find the maximum length of the marathon.
    Parameters:
        root (TreeNode): The root of the binary tree
    Returns:
        int: The maximum length of the marathon
    """
    diameter = 0  # This will store the final answer
    
    stack = [(root, False)]  # Iterative post-order stack
    heights = {}  # Store heights of nodes
    
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)
            heights[node] = 1 + max(left_height, right_height)
            diameter = max(diameter, left_height + right_height)
        else:
            stack.append((node, True))
            stack.append((node.left, False))
            stack.append((node.right, False))
    
    return diameter

    """
    Write your logic here to find the maximum length of the marathon.
    Parameters:
        root (TreeNode): The root of the binary tree
    Returns:
        int: The maximum length of the marathon
    """
    pass

def construct_tree(i, nodes):
    if i < 0 or i >= len(nodes) or nodes[i] is None:
        return None
    node = TreeNode(i + 1)
    if nodes[i][0] != -1:
        node.left = construct_tree(nodes[i][0] - 1, nodes)
    if nodes[i][1] != -1:
        node.right = construct_tree(nodes[i][1] - 1, nodes)
    return node

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of landmarks
    nodes = []
    for i in range(n):
        l = int(data[2 * i + 1])
        r = int(data[2 * i + 2])
        nodes.append((l, r))
    
    # Construct the binary tree
    root = construct_tree(0, nodes)
    
    # Call user logic function and print the output
    result = user_logic(root)
    print(result)

if __name__ == "__main__":
    main()

#INCOMPLETE SUBMISSION 82/100