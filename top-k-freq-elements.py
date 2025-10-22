class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1

        sorted_n = sorted(hash, key=hash.get, reverse=True)
        print(sorted_n)
        return sorted_n[:k]
