from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = sorted(Counter(tangerine).items(), reverse=True, key= lambda x: x[1])
    for key, val in count:
        if k <=0:
            break
        k -= val
        answer += 1
    return answer