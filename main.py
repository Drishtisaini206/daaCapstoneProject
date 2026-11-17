from dataset import generate_parcels, generate_graph
from sorting import merge_sort_parcels
from knapsack import solve_knapsack
from routing import dijkstra, nearest_neighbor_tsp

def main():
    print("==================================================")
    print("   DAA Capstone Project: Courier Delivery System   ")
    print("==================================================\n")
    
    # Step 1: Generate Data
    parcels = generate_parcels(8)
    graph = generate_graph()
    print(f"[1] Generated {len(parcels)} raw parcels and city delivery graph.")
    
    # Step 2: Sort Parcels
    sorted_parcels = merge_sort_parcels(parcels, key='deadline')
    print(f"\n[2] Sorted Parcels by Deadline (Merge Sort):")
    for p in sorted_parcels:
        print(f"    - ID: {p['id']} | Deadline: {p['deadline']}h | Weight: {p['weight']}kg | Value: ${p['value']} | Dest: {p['destination_node']}")
        
    # Step 3: Knapsack Selection
    max_capacity = 12
    selected_parcels, total_value = solve_knapsack(sorted_parcels, max_capacity)
    print(f"\n[3] Optimal Parcels Selected (0/1 Knapsack | Max Capacity: {max_capacity}kg | Total Value: ${total_value}):")
    for p in selected_parcels:
        print(f"    - ID: {p['id']} | Weight: {p['weight']}kg | Dest: {p['destination_node']}")
        
    # Step 4: Graph Routing (Dijkstra + TSP)
    distances = dijkstra(graph, 'Depot')
    
    # Build distance matrix sub-dictionary for selected destinations + Depot
    selected_destinations = list(set([p['destination_node'] for p in selected_parcels] + ['Depot']))
    sub_matrix = {}
    for d1 in selected_destinations:
        sub_matrix[d1] = {}
        d1_distances = dijkstra(graph, d1)
        for d2 in selected_destinations:
            if d1 == d2:
                sub_matrix[d1][d2] = 0
            else:
                sub_matrix[d1][d2] = d1_distances.get(d2, 999)
                
    route, total_distance = nearest_neighbor_tsp(sub_matrix, 'Depot')
    print(f"\n[4] Final Optimal Delivery Route (TSP Heuristic):")
    print(f"    {' -> '.join(route)}")
    print(f"    Total Route Distance: {total_distance} km")
    print("\n==================================================")
    print("Pipeline Execution Complete!")

if __name__ == '__main__':
    main()
    