def solve_knapsack(parcels, max_capacity):
    """Applies 0/1 Knapsack DP to find optimal parcels fitting within weight capacity."""
    n = len(parcels)
    dp = [[0 for _ in range(max_capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight = parcels[i-1]['weight']
        value = parcels[i-1]['value']
        
        for w in range(1, max_capacity + 1):
            if weight <= w:
                dp[i][w] = max(value + dp[i-1][w - weight], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    # Traceback to select optimal parcels
    w = max_capacity
    selected_parcels = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_parcels.append(parcels[i-1])
            w -= parcels[i-1]['weight']
            
    return selected_parcels, dp[n][max_capacity]
