class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0] * n
        stack = []  # Pairs of (index, temp) can be used, but storing just indices is more memory efficient
        
        for i in range(n):
            current_temp = temperatures[i]
            
            # Pop from the stack as long as the current temperature is warmer
            # than the temperature at the index on top of the stack
            while stack and current_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
                
            stack.append(i)
            
        return ans