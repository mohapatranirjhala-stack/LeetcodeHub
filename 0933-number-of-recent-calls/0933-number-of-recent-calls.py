class RecentCounter:

    def __init__(self):
        # Initialize an empty double-ended queue to store timestamps
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Step 1: Add the current timestamp to the end of the queue
        self.requests.append(t)
        
        # Step 2: Remove all timestamps that are older than t - 3000 from the front
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
            
        # Step 3: The size of the queue represents the number of recent calls
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)