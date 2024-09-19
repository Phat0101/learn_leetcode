from collections import defaultdict

def countSubTrees(n, edges, labels):
    # Build the tree using adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # Result array to store the count of labels in each subtree
    result = [0] * n
    
    # DFS function to traverse the tree and count labels
    def dfs(node, parent):
        # Dictionary to count labels in the current subtree
        count = defaultdict(int)
        count[labels[node]] += 1
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_count = dfs(neighbor, node)
            for label, cnt in child_count.items():
                count[label] += cnt
        
        result[node] = count[labels[node]]
        return count
    
    # Start DFS from the root node (0)
    dfs(0, -1)
    
    return result