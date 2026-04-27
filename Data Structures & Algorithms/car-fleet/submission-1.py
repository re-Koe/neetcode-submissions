class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        atuple = [(pos, spe) for pos, spe in zip(position, speed)]
        atuple.sort(reverse=True)
        stack = []

        for pos, spe in atuple:
            stack.append((target - pos)/spe)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


