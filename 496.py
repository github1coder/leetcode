class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        t=[]
        le=len(nums2)
        for i in range(le):
            dic[nums2[i]]=-1
            for j in range(i+1,le):
                if nums2[j]>nums2[i]:
                    dic[nums2[i]]=nums2[j]
                    break
        for num in nums1:
            t.append(dic[num])
        return t

            
