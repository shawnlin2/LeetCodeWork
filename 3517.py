
def smallestPalindrome(s: str) -> str:
    letter_code = [0 for i in range(26)]
    for letter in s:
        index = ord(letter) - 97
        letter_code[index] += 1
    res = ""
    left = ""
    right = ''
    for ind in range(len(letter_code)):
        letter = chr(ind + 97)
        count = letter_code[ind] // 2
        left += letter * count
        right = letter * count + right
        if letter_code[ind] % 2 == 1:
            res += letter
        
            
    return left + res + right

tests = ["z","babab", "daccad", "cccccll"]
for test in tests:
    print(smallestPalindrome(test))