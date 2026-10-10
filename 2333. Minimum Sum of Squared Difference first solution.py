class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        ans = 0
        n = len(nums1)
        diff = []
        ma =[]
        for i in range(n):
            diff.append(abs(nums1[i] - nums2[i]))
        indices = sorted(range(n), key=lambda i: diff[i])
        indices = indices[::-1]
        for k in range(n-1):
            ma.append(diff[indices[k]] - diff[indices[k+1]])
        for j in range(k1):

            if nums1[indices[0]] >= nums2[indices[0]]:
                nums1[indices[0]] -= 1
            else:
                nums1[indices[0]] += 1
        print(diff)
        print(ma)
        print(indices)
        print(nums1)
        return ans
        
