import time
import matplotlib.pyplot as plt
from dataset import generate_parcels, generate_graph
from sorting import merge_sort_parcels
from knapsack import solve_knapsack

def run_benchmarks():
    sizes = [10, 50, 100, 500, 1000]
    runtimes = []
    
    print("Running performance benchmarks...")
    for n in sizes:
        parcels = generate_parcels(n)
        start_time = time.perf_counter()
        
        # Benchmark sorting and knapsack pipeline
        sorted_p = merge_sort_parcels(parcels, key='deadline')
        solve_knapsack(sorted_p, max_capacity=20)
        
        end_time = time.perf_counter()
        runtimes.append((end_time - start_time) * 1000) # Convert to milliseconds
        
    # Plotting results
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, runtimes, marker='o', color='purple', linestyle='-', linewidth=2)
    plt.title('DAA Capstone Pipeline Execution Time')
    plt.xlabel('Dataset Size (Number of Parcels)')
    plt.ylabel('Execution Time (ms)')
    plt.grid(True)
    plt.savefig('runtime_performance.png')
    print("Benchmark chart saved successfully as 'runtime_performance.png'.")

if __name__ == '__main__':
    run_benchmarks()