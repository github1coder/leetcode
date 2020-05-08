class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)
        if m>n:
            nums1,nums2,n,m=nums2,nums1,m,n
        imi,ima,half=0,m,(m+n+1)//2
        while imi<=ima:
            i=(imi+ima)//2
            j=half-i
            if i <m and nums2[j-1]>nums1[i]:
                imi=i+1
            elif i>0 and nums1[i-1] > nums2[j]:
                ima=i-1
            else:
                if i==0:
                    male=nums2[j-1]
                elif j==0:
                    male=nums1[i-1]
                else:
                    male=max(nums2[j-1],nums1[i-1])
                if (m+n)%2==1:
                    return male
                if i==m :
                    miri=nums2[j]
                elif j==n:
                    miri=nums1[i]
                else:
                    miri=min(nums1[i],nums2[j])
                return (male+miri)/2.0