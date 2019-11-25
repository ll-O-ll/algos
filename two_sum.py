class Solution(object):
    def __init__(self):
        pass
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Given nums = [2, 7, 11, 15], target = 9,
        # Because nums[0] + nums[1] = 2 + 7 = 9,
        # return [0, 1].
        # if not nums:
        #     return nums

        lis = nums
        output = []

        for i in range(len(nums)):
            for j in range(i+1,(len(lis))):
                sum = lis[j] + nums[i]
                if sum == target:
                    output.append(i)
                    output.append(j)
                    return output 

if __name__ == "__main__":
    
    #input params

    input = [3,2,4]
    target = 6

    s = Solution()
    #run the class...
    print(s.twoSum(input,target))
