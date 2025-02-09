# class NumberContainers:

#     def __init__(self):
        

#     def change(self, index: int, number: int) -> None:
        

#     def find(self, number: int) -> int:
#         import heapq
from collections import defaultdict

class NumberContainers:
    def __init__(self):
        # Mapping from index to the current number at that index.
        self.index_to_number = {}
        # Mapping from number to a min-heap of indices that currently hold that number.
        self.num_to_indices = defaultdict(list)
    
    def change(self, index: int, number: int) -> None:
        self.index_to_number[index] = number
        heapq.heappush(self.num_to_indices[number], index)
    
    def find(self, number: int) -> int:
        if number not in self.num_to_indices:
            return -1
        
        heap = self.num_to_indices[number]
        # Lazy removal of indices that no longer have the value 'number'
        while heap and self.index_to_number.get(heap[0]) != number:
            heapq.heappop(heap)
        
        return heap[0] if heap else -1
