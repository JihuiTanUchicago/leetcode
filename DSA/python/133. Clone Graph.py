"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        visited = set()
        node_hashmap = {}
        stack = [node]
        visited.add(node.val)
        while stack != []:
            cur_node = stack.pop(0)
            if node_hashmap.get(cur_node.val, None) == None:
                cur_node_copy = Node(val=cur_node.val)
                node_hashmap[cur_node.val] = cur_node_copy
            else:
                cur_node_copy = node_hashmap[cur_node.val]
            for neighbor in cur_node.neighbors:
                if neighbor.val not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor.val)
                    new_node = Node(val=neighbor.val)
                    node_hashmap[neighbor.val] = new_node
                else:
                    new_node = node_hashmap[neighbor.val]
                   
                cur_node_copy.neighbors.append(new_node)

        return node_hashmap[1]
