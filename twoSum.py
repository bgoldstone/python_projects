def twoSum(self, nums: List[int], target: int) -> List[int]:
  for i in range(len(nums)):
    n1 = int(target - nums[i])
    if (n1 in nums) and i != nums.index(n1):
      return [i,nums.index(n1)]
