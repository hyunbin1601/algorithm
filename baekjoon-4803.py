import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    parent = {start: None}
    is_tree = True
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)
            else:
                if parent[node] != neighbor:
                    is_tree = False
                    
    return is_tree

def main():
    case = 1
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        graph = defaultdict(list)
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
            
        visited = [False] * (n + 1)
        trees = 0
        
        for i in range(1, n + 1):
            if not visited[i]:
                if bfs(i, graph, visited):
                    trees += 1
                    
        if trees == 0:
            print(f"Case {case}: No trees.")
        elif trees == 1:
            print(f"Case {case}: There is one tree.")
        else:
            print(f"Case {case}: A forest of {trees} trees.")
            
        case += 1
        
if __name__ == "__main__":
    main()
    