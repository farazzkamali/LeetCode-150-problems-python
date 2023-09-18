class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while stones:
            if len(stones) == 1:
                return stones[0]
            stones.sort()

            stone_one = stones[-2]
            stone_two = stones[-1]

            stones.pop()
            stones.pop()

            if stone_two > stone_one:
                new_stone = stone_two - stone_one
                stones.append(new_stone)

        return 0
