class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice, sumBob = sum(aliceSizes), sum(bobSizes)
        setBob = set(bobSizes)
        for x in aliceSizes:
            if x + (sumBob - sumAlice) // 2 in setBob:
                return [x, x + (sumBob - sumAlice) // 2]