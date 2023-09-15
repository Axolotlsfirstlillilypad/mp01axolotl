"""
Problem: Zigzag Level Order Traversal of Binary Tree

Description:
Given a binary tree, populate an array to represent its zigzag level order traversal. Populate the values of all nodes of the first level from left to right, then right to left for the next level, and keep alternating in the same manner for the subsequent levels.

Function Signature:
def zigzag_level_order_traversal(root: TreeNode) -> List[List[int]]:

Inputs:
    - root (TreeNode): The root node of the binary tree. The TreeNode is defined as:
        class TreeNode:
            def __init__(self, value=0, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right

Returns:
    - List[List[int]]: A list where each inner list contains the values of the nodes for each level in a zigzag order.

Examples:

1. Input:
        Tree Structure:
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
   Output: [[1], [3, 2], [4, 5, 6, 7]]

2. Input:
        Tree Structure:
           12
         /    \
        7     1
       /     / \
      9     10  5
   Output: [[12], [1, 7], [9, 10, 5]]

Notes:
    - Use a queue for BFS. Process each level of nodes, reversing the order for every other level to achieve the zigzag pattern.
    - A flag can be used to indicate the direction of traversal at each level (left-to-right or right-to-left).

Tags:
    - Trees
    - Queue
"""

from typing import List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_level_order_traversal(root: TreeNode) -> List[List[int]]:
    if root is None:
        return []

    nodes = []
    heir = []

    flag=0
 
    nodes.append(root)

    list2=[[root.value]]
    
   
    while len( nodes) > 0:

       
        temp =  nodes.pop()

 
        if flag==1:
            if temp.left:
                heir.append(temp.left)
            if temp.right:
                heir.append(temp.right)
                
        else:
            if temp.right:
                
                heir.append(temp.right)
            if temp.left:
                heir.append(temp.left)
 
        if len(nodes) == 0:
            flag=(flag+1)%2
            list3=[]
            for i in range(len(heir)):
                    list3.append(heir[i].value)
            
        
            list2.append(list3)
            nodes, heir = heir,  nodes
        
        
    return list2[:len(list2)-1]
