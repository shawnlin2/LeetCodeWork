def generateKey(num1: int, num2: int, num3: int) -> int:
        res = 0
        count = 0
        while num1 > 0 or num2 > 0 or num3 > 0:
            num = min(num1 % 10, num2 % 10, num3 % 10)
            res = res + (num * 10 ** count)
            num1 = num1 // 10
            num2 = num2 // 10
            num3 = num3 // 10
            count += 1
        return res
print(generateKey(num1 = 1, num2 = 10, num3 = 1000))
print(generateKey(num1 = 987, num2 = 879, num3 = 798))
print(generateKey(num1 = 1, num2 = 2, num3 = 3))