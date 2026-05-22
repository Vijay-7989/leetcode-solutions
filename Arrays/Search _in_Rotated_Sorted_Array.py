class Solution:
    def search(self, nums: List[int], target: int) -> int:
      """
      using two pointer approach
      """
        # left = 0 
        # right = len(nums)-1
        # while(left<=right):
        #     if nums[left] == target:
        #         return left
        #     if nums[right] == target:
        #         return right
        #     left+=1
        #     right-=1
        # return -1
      """
      using modified binary search approach
      """
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[left]<=nums[mid]:
                if nums[left] <= target <=nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid] <= target <=nums[right]:
                    left = mid+1
            else:
                right =mid-1
        return -1

            

        
