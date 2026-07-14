class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        m[:] = map(list,zip(*m[::-1]))