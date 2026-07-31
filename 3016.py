import heapq
def minimumPushes(word: str) -> int:
    priority_queue = []
    letter_map = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
        'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
        's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
    }
    
    
    res = 0
    for letter in word:
        
        letter_map[letter] += 1
    for key, value in letter_map.items():
        if value != 0:
            heapq.heappush(priority_queue, (value, key))

    ind = (len(priority_queue) // 8)
    count = 8
    if len(priority_queue) % 8 > 0:
        count = len(priority_queue) % 8
        ind += 1
    while priority_queue:
        val , letter = heapq.heappop(priority_queue)
        res += val * ind
        count -= 1
        if count < 1:
            count = 8
            ind -= 1
    return res

        


tests = [('abcde', 5), ('xyzxyzxyzxyz', 12), ("aabbccddeeffgghhiiiiii", 24), ("qwertyuiopasdfghjklzxcvbnm", 56)]
for test in tests:
    print(test[0])
    val = minimumPushes(test[0])
    print(test[1], val)
    if val == test[1]:
        print("Passed")
    else:
        print("Failed")


