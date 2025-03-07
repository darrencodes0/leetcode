class Solution:
  def productExceptSelf(self, nums : list[int]):
    nums2 = []

    for i in range(len(nums)):
      j = 0
      productExceptSelf = 1

      while(j < len(nums)):
        if i != j:
          productExceptSelf = nums[j] * productExceptSelf
          print(productExceptSelf)

        j += 1
      
      nums2.append(productExceptSelf)

    print(nums2)



if __name__ == '__main__':
  solution = Solution()
  solution.productExceptSelf([-1,1,0,-3,3])


  """
  Solution:
  I did O(N^2) solution however it requiers O(N). I found a way to do O(N) thorugh a video but only konw
  the brute force strategy. https://www.youtube.com/watch?v=bNvIQI2wAjk, this is the O(N) solution and uses prefix
  and postfix sum in order to solve this. Using two pointers for both the beginning and end of the array, you can

  O(N) - multiply all the prefix and postfix values with a initized array with 1's of the same length of nums array"""