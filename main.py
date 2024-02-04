from typing import List

class Solution:
    def  threeSum(Self, nums: List[int]) -> List[List[int]]:
        result = [] 
        nums.sort() # soterd the array !
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue # same value twice, skip it
            left, right = i+1, len(nums)-1 
            # right = end of the list
            
            while left < right:
               threeSum =  a + nums[left]+ nums[right]
               if threeSum >0:
                   right-=1
               elif threeSum <0:
                   left +=1
               else:
                   result.append([a, nums[left], nums[right]]) 
                   left +=1
                   while nums[left] == nums [left -1]:
                       left +=1
        return result
    
        # [0,1,2,3,4,5]          
        # [-2,-2,0,0,2,2]
        # i > 0 => i = -2 in position 1
        # a = -2 in position 0
        # if a == nums[i]  continue, so we will skip the -2 in position 1
        # left = i+1 = 1, right = 5 - 1 = 4 (starts from 0-4)
        # while (left < right)
        # threeSum = a + nums[left]+ nums[right] = -2 +0 +2    
        # append it to result
def main():
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    result = solution.threeSum(nums)
    print(result)
    solution = Solution()
    nums = [-2, -2, 0, 0, 2, 2]
    result = solution.threeSum(nums)
    print(result)

if __name__ == "__main__":
    main()