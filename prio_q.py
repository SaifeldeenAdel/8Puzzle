import heapq as pq


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, obj, priority):
        pq.heappush(self.heap, (priority, obj))

    def pop(self):
        return pq.heappop(self.heap)[1]

    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        sorted_heap = sorted(self.heap)
        return iter(sorted_heap)

    def contains(self, item):
        # Check if an item exists in the heap
        return any(item == obj for _, obj in self.heap)
