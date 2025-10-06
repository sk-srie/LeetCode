from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in h:
                return (h[complement], i)
            h[num] = i
        return [-1, -1]

if __name__  == "__main__":
    nums = list(map(int, input("Enter space seperated numbers: ").split()))
    target = int(input("Enter target number: "))
    sol = Solution()
    print(sol.twoSum(nums, target))