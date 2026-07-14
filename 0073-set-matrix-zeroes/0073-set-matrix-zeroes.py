class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
       R=[i for i,r in enumerate(m) if 0 in r]
       C=[j for j,c in enumerate(zip(*m)) if 0 in c]

       for i in R:
           m[i]=[0]*len(m[0])
    
       for j in C:
           for r in m:
               r[j] = 0