class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set = set()
        for i in nums:
            if i in nums_set:
                nums.remove(i)
            nums_set.add(i)
        answer = list(nums_set)
        return len(answer), answer
        