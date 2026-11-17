import heapq

def dijkstra(graph, start_node):
    """Computes shortest paths from start_node to all other nodes using Dijkstra's algorithm."""
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    pq = [(0, start_node)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

def nearest_neighbor_tsp(distance_matrix, start_node='Depot'):
    """Approximates Traveling Salesperson Problem route for delivery locations."""
    unvisited = set(distance_matrix.keys())
    current = start_node
    route = [current]
    unvisited.remove(current)
    total_distance = 0
    
    while unvisited:
        next_node = min(unvisited, key=lambda node: distance_matrix[current].get(node, float('inf')))
        total_distance += distance_matrix[current][next_node]
        current = next_node
        route.append(current)
        unvisited.remove(current)
        
    # Return trip back to Depot
    total_distance += distance_matrix[current][start_node]
    route.append(start_node)
    return route, total_distance