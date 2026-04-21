class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                final[stackInd] = i - stackInd
            stack.append((t, i))
        return final