1971. Find if Path Exists in Graph
There is a bi-directional graph with n vertices, where each vertex is labeled from
0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array
edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui
and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has
an edge to itself.
You want to determine if there is a valid path that exists from vertex source to
vertex destination.
Given edges and the integers n, source, and destination, return true if there is a
valid path from source to destination, or false otherwise.

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True
        d={i:[] for i in range(n)}
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        q=[source]
        vis=set()
        while q:
            a=q.pop(0)
            for i in d[a]:
                if i==destination:
                    return True
                if i not in vis:
                    q.append(i)
                    vis.add(i)
        return False    
      

