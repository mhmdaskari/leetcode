class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
     
        i_m = m-1
        i_n = n-1
        i_k = m+n-1

        while i_m >=0 and i_n >= 0:
            if nums1[i_m] < nums2[i_n]:
                nums1[i_k] = nums2[i_n]
                i_n -= 1
            else:
                nums1[i_k] = nums1[i_m]
                i_m -= 1
            
            i_k -= 1
        
        while i_n>=0:
            nums1[i_n] = nums2[i_n]
            i_n -= 1
