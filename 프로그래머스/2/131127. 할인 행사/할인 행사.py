def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        tmp = discount[i:i+10]
        cnt = 0
        for w, n in zip(want, number):
            if tmp.count(w) < n:
                break
            else:
                cnt += n
        if cnt == sum(number):
            answer += 1
    return answer