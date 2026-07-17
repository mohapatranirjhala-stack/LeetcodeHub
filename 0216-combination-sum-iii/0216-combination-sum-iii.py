class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        
        def backtrack(remain_sum: int, start: int, current_comb: List[int]):
            # Base Case 1: If combination matches the required size
            if len(current_comb) == k:
                if remain_sum == 0:
                    results.append(list(current_comb))
                return
            
            # Base Case 2: If sum exceeded or no more digits left to choose from
            if remain_sum < 0:
                return
                
            # Iterate through valid single-digit candidates (1 through 9)
            for i in range(start, 10):
                current_comb.append(i)                           # Choose i
                backtrack(remain_sum - i, i + 1, current_comb)   # Recurse with next digit
                current_comb.pop()                               # Backtrack
                
        # Start backtracking from digit 1 with an empty combination list
        backtrack(n, 1, [])
        return results