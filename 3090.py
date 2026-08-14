def maximumLengthSubstring(s: str) -> int:
    letter_count = {letter: 0 for letter in set(s) }
    pointer = 0
    largest = 0
    for ind in range(len(s)):
        letter = s[ind]
        if letter_count[letter] < 2:
            letter_count[letter] += 1
        else:
            largest = max(ind - pointer, largest)
            while pointer < ind and s[pointer] != letter:
                pointer_letter = s[pointer]
                letter_count[pointer_letter] -= 1
                pointer += 1
            
            pointer += 1
    return max(largest, len(s) - pointer)

tests = [("bcbbbcba", 4), ("aaaa", 2), ('a', 1), ("abcde", 5) ]
for word, expected in tests:
    res = maximumLengthSubstring(word)
    print(f'Got: {res}\nExpected: {expected}')
    if res == expected:
        print("Passed\n")
    else:
        print('Failed\n')
    
