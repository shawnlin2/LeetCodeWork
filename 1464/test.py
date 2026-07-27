def maxProduct(nums: list[int]) -> int:
        max1 = 0
        max2 = 0
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            else:
                max2 = max(max2, num)
        return (max1 - 1) * (max2 - 1)
import random as rand
tests = [
     [3,4,5,2], [1,5,4,5], [1,1,1,1], [9, 2], [rand.randint(1, 10) for i in range(500)]
        ]
for test in tests:
     print(test)
     print(maxProduct(test))