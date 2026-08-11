def smallestNumber( n: int, t: int) -> int:
    for i in range(n, 101):
        val = 1
        current = i
        while current > 0:
            val *= current % 10
            current = current // 10
        if val % t == 0:
            return i