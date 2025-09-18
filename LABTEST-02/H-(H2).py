import heapq

def dijkstra(graph, source):
    # Step 1: Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Step 2: Use a priority queue to select the next node with the smallest distance
    pq = [(0, source)]  # (distance, node)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Step 3: Edge relaxation for all neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage:
if __name__ == "__main__":
    graph = {'A':{'B':1,'C':4},'B':{'C':2,'D':5},'C':{'D':1},'D':{}}
    print(dijkstra(graph, 'A'))