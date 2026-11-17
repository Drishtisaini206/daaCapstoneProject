def generate_parcels(n=10):
    """Generates a list of n sample parcels with weight, value, deadline, and destination."""
    import random
    parcels = []
    destinations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in range(1, n + 1):
        parcels.append({
            'id': f'P{i}',
            'weight': random.randint(1, 10),
            'value': random.randint(10, 100),
            'deadline': random.randint(1, 5),
            'destination_node': destinations[(i - 1) % len(destinations)]
        })
    return parcels

def generate_graph():
    """Generates a sample graph dictionary representing delivery locations and distances."""
    return {
        'Depot': {'A': 4, 'B': 2},
        'A': {'Depot': 4, 'B': 1, 'C': 5},
        'B': {'Depot': 2, 'A': 1, 'D': 8, 'E': 10},
        'C': {'A': 5, 'F': 2},
        'D': {'B': 8, 'F': 3, 'G': 1},
        'E': {'B': 10, 'G': 2},
        'F': {'C': 2, 'D': 3, 'H': 4},
        'G': {'D': 1, 'E': 2, 'H': 3},
        'H': {'F': 4, 'G': 3}
    }