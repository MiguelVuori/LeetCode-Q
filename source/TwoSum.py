class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, j in enumerate(nums):
            if j in d:        
                r = []
                r.append(i)
                r.append(d[j])
                return r
            else:
                d[target - j] = i
                j += 1