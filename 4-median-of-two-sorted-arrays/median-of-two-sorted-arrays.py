class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
        i,j=0,0
        k=[]
        while i< len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                k.append(nums1[i])
                i+=1
            else:
                k.append(nums2[j])
                j+=1
        if i<len(nums1):
            k.extend(nums1[i:])
        if j<len(nums2):
            k.extend(nums2[j:])
        n=len(k)
        midIndex=n//2
        if n%2==0:
            return (k[midIndex]+k[midIndex-1])/2
        else:
            return k[midIndex]
        