class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k=0
        i_r=0
        i_w=0

        while i_r < len(nums):
            if nums[i_r] != val:
                nums[i_w] = nums[i_r]
                i_w+= 1
                k+=1
            
            i_r+=1    
        
        return k
        