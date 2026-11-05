class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        result = []

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums_sorted) - 1

            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue

            while j < k:
                curr_sum = nums_sorted[i] + nums_sorted[j] + nums_sorted[k]

                if curr_sum == 0:
                    result.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                    j += 1
                    k -= 1

                    while j < k and nums_sorted[j] == nums_sorted[j-1]:
                        j += 1
                    
                    while j < k and nums_sorted[k] == nums_sorted[k+1]:
                        k -= 1
                    

                elif curr_sum < 0:
                    j += 1
                
                else:
                    k -= 1  

        return result
            
        