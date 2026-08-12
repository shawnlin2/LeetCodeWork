def maxSubarrayLength(nums: list[int], k: int) -> int:
        current_sub = {num : 0 for num in set(nums)}
        
        pointer = 0
        largest_len = 0
        for i in range(len(nums)):
            value = nums[i]
            
            if current_sub[value] == k:
                largest_len = max(largest_len, i - pointer)
                while nums[pointer] != value:
                    current_sub[nums[pointer]] -= 1
                    pointer += 1
                pointer += 1

            else:
                current_sub[value] += 1
        return max(largest_len, i - pointer + 1)

tests = [([1,2,3,1,2,3,1,2], 2), ([1,2,1,2,1,2,1,2], 1), ([5,5,5,5,5,5,5], 4), ([1,2,3,4,5,6,7,8,9], 1)]
for test in tests:
    print( maxSubarrayLength(test[0], test[1]))