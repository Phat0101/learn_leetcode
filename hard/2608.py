from collections import defaultdict
from collections import deque
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        shortest_length = 1001

        def bfs(start_vertex):
            visited = [-1] * n
            queue = deque([(start_vertex, -1, 0)])
            visited[start_vertex] = 0
            shortest = 1001
            while queue:
                current, parent, dist = queue.popleft()
                for neighbor in graph[current]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = dist + 1
                        queue.append((neighbor, current, dist + 1))
                    elif neighbor != parent:
                        shortest = min(dist + visited[neighbor] + 1, shortest)
                        if shortest == 3:
                            return 3
            return shortest

        for i in range(n):
            shortest_length = min(shortest_length, bfs(i))
            if shortest_length ==3:
                return 3
        return shortest_length if shortest_length != 1001 else -1
                


        return 0