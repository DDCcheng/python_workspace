class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_map={}
        i=0
        for i in range(len(nums)):
            num=target-nums[i]
            if my_map.__contains__(num):
                return [i,my_map[num]]
            my_map[nums[i]]=i
            i+=1
        return []

my=Solution()
print(my.twoSum([2,7,11,15],9))