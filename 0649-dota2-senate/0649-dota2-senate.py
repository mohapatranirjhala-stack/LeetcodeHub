class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        
        # Step 1: Populate queues with initial indices
        for i, char in enumerate(senate):
            if char == 'R':
                radiant.append(i)
            else:
                dire.append(i)
                
        # Step 2: Simulate the banning rounds
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            
            # The senator with the lower index bans the other
            if r_idx < d_idx:
                # Radiant bans Dire. Radiant goes to the back for the next round.
                radiant.append(r_idx + n)
            else:
                # Dire bans Radiant. Dire goes to the back for the next round.
                dire.append(d_idx + n)
                
        # Step 3: Whoever has remaining senators wins
        return "Radiant" if radiant else "Dire"