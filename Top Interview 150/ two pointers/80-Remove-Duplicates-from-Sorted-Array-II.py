class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        element_one = nums[0]
        ir=1
        iw=1
        repeat=1
        k=1

        while ir < len(nums):
            element_two = nums[ir]

            if element_two == element_one:
                repeat+=1
                if repeat == 2:
                    nums[iw] = element_two
                    iw += 1
                    k += 1
            elif element_two > element_one:
                nums[iw] = element_two
                iw += 1
                k += 1
                repeat = 1

            element_one = element_two
            ir += 1

        return k

            
