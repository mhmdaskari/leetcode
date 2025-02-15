class Solution(object):
    def merge(self, nums1, m, nums2, n):
        \\\
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
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
        
        # elif i_2<0:
        #     pass
