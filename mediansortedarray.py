def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1+nums2)
        if len(nums)%2 == 0:
            print (nums[len(nums)/2],nums[len(nums)/2-1])
            return (nums[len(nums)/2]+nums[len(nums)/2-1])/2.0
        else:
            return nums[len(nums)/2]


print(findMedianSortedArrays([1,2],[3,4]))
