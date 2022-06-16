class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_elmnt_num1 = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last_elmnt_num1] = nums1[m-1]
                m-=1
            else:
                nums1[last_elmnt_num1] = nums2[n-1]
                n-=1
            last_elmnt_num1-=1
        while n > 0:
            nums1[last_elmnt_num1] = nums2[n-1]
            n, last_elmnt_num1 = n-1, last_elmnt_num1-1
            
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

