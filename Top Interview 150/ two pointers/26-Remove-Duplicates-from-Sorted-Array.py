class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        iw=1
        ir=1
        pre_value=nums[0]
        k=1

        while ir < len(nums):
            next_value = nums[ir]

            if next_value == pre_value:
                ir += 1
            else:
                nums[iw] = next_value
                iw += 1
                ir += 1
                k += 1

            pre_value = next_value

        return k