def minimumPushes(word: str) -> int:
    inst = len(word) // 8
    res = (len(word) % 8) * (inst + 1)
    for i in range(inst):
        res += (i + 1) * 8
    return res 

test = 'qwertyuiopasdfghjklzxcvbnm'
for i in range(len(test)):
    print(f'{test[0:i + 1]}: {minimumPushes(test[0:i + 1])}')
    
