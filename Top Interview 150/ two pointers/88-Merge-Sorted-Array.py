class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        \\\
        Do not return anything, modify nums1 in-place instead.
        \\\
        
        i_1 = m-1
        i_2 = n-1
        j = m+n-1

        while i_1>-1 and i_2>-1:
            if nums1[i_1] >= nums2[i_2]:
                nums1[j] = nums1[i_1]
                i_1-=1
            
            else:
                nums1[j] = nums2[i_2]
                i_2-=1
            
            j-=1

        if i_1<0:
            nums1[0:j+1] = nums2[0:i_2+1]