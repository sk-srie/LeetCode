class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = [nums[0]]
        for i in range(len(nums)):
            if i == 0:
                continue
            self.prefixSum.append(self.prefixSum[i - 1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if (left == 0):
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left - 1]