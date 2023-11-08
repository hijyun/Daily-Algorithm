def solution(s):
    answer = [0, 0]
    while len(s) > 1:
        answer[0] += 1
        zero_cnt = s.count('0')
        answer[1] += zero_cnt
        s = (len(s) - zero_cnt) * '1'
        s = bin(len(s))[2:]
        


    
    

    return answer