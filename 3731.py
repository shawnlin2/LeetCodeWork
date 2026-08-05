
def findMissingElements(nums: list[int]) -> list[int]:
    small = min(nums)
    big = max(nums)
    numbers = [False for i in range(small, big + 1)]
    for num in nums:
        numbers[num - small] = True
    res = []
    for ind in range(len(numbers)):
        if not numbers[ind]:
            res.append(ind + small)
    return res

tests = [[1,4,2,5], [7,8,6,9], [5,1], [2,1], [1,100,98,2]]
for test in tests:
    print(findMissingElements(test))