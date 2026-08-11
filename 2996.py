
def missingInteger(nums: list[int]) -> int:
    large_sum = nums[0]
    pointer = 1
    while pointer < len(nums) and nums[pointer - 1] + 1 == nums[pointer]:
        large_sum += nums[pointer]
        pointer += 1
    nums.sort()
    for num in nums:
        if num > large_sum:
            return large_sum
        elif num == large_sum:
            large_sum += 1
    return large_sum
tests = [[1,2,3,2,5], [3,4,5,1,12,14,13], [1,2,3,4,5], [1,3,4]]
for test in tests:
    print(missingInteger(test))
