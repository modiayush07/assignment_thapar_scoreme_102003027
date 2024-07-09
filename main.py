def longest_path(graph: list) -> int:
    def topological_sort(graph):
        n = len(graph)
        in_degree = [0] * n
        for u in range(n):
            for v, w in graph[u]:
                in_degree[v] += 1
                
        stack = [u for u in range(n) if in_degree[u] == 0]
        topo_order = []
        
        while stack:
            u = stack.pop()
            topo_order.append(u)
            for v, w in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    stack.append(v)
        
        return topo_order
    
    def calculate_longest_path(graph, topo_order):
        n = len(graph)
        dist = [0] * n
        for node in topo_order:
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
        return max(dist)
    
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)