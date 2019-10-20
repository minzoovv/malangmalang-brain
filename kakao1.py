def solution(s):
    result = len(s)
    for i in range(1, (len(s) // 2) + 1):
        total = len(s)
        target = s[0:i]
        duplicate = 1
        for count in range(i, len(s), i):
            if target == s[count:count+i]:
                duplicate += 1
                if duplicate >= 2:
                    total -= i
            else:
                if duplicate > 1:
                    total += len(str(duplicate))
                duplicate = 1
                target = s[count:count+i]
        if duplicate > 1:
            total += len(str(duplicate))
        result = min(result, total)
    return result

result = solution(input())
print(result)