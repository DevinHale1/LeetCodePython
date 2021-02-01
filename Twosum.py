class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target = 9
        test = 0
        nums = [2,7,11,15]
        count = 0
        count1 = 1
        solution = []
        while test != target:
        
            test = nums[count] + nums[count1]
            if test == target:
                solution.append(count)
                solution.append(count1)
                return solution

            else:
                count1 +=1
                if count1 == count:
                    count1 +=1
                               
            if count1 > len(nums) - 1:
                count +=1
                count1 = 0
                
            if count1 and count > len(nums) -1:
                return "No solution"
