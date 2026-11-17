def merge_sort_parcels(parcels, key='deadline'):
    """Sorts parcels by deadline or priority using Merge Sort ($O(n \log n)$)."""
    if len(parcels) <= 1:
        return parcels
    
    mid = len(parcels) // 2
    left = merge_sort_parcels(parcels[:mid], key)
    right = merge_sort_parcels(parcels[mid:], key)
    
    return merge(left, right, key)

def merge(left, right, key):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Sort ascending for deadline, descending for value/priority
        condition = left[i][key] < right[j][key] if key == 'deadline' else left[i][key] > right[j][key]
        if condition:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list