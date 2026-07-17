import heapq

class SmallestInfiniteSet:

    def __init__(self):
        # Tracks the smallest integer that hasn't been popped yet
        self.current = 1
        # Heap to track numbers that were popped and then added back
        self.added_back_heap = []
        # Set to prevent adding duplicate numbers back into the heap
        self.added_back_set = set()

    def popSmallest(self) -> int:
        # If there are elements that were added back, the smallest one is in the heap
        if self.added_back_heap:
            smallest = heapq.heappop(self.added_back_heap)
            self.added_back_set.remove(smallest)
            return smallest
        
        # Otherwise, the smallest element is the current threshold pointer
        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        # We only add back if the number is smaller than the current frontier pointer
        # and it isn't already waiting in our added_back collections
        if num < self.current and num not in self.added_back_set:
            heapq.heappush(self.added_back_heap, num)
            self.added_back_set.add(num)