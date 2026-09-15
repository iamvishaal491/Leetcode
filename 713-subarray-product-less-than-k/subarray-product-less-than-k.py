class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0

        left=0
        win=1
        count=0

        for right in range(len(nums)):
            win*=nums[right]

            while win>=k:
                win//=nums[left]
                left+=1
                
            count+=right-left+1

        return count

        