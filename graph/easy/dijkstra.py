import heapq

def dijkstra(graph, start):
    # graph is a dictionary where each key is a node and value is list of (neighbor, weight)
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    visited = set()
    heap = [(0, start)]  # (distance, node)

    while heap:
        curr_dist, node = heapq.heappop(heap) # heappop removes the smallest node that has the smallest distance

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))

    return dist 


# Time Complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges
# why log V? because we are using a priority queue (min-heap) to store the vertices
# and we need to pop the smallest element from the heap which takes log V time
# Space Complexity: O(V) where V is the number of vertices and used heap to store the vertices

# Example usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    print(f"Shortest distances from {start_node}: {distances}")