def solution(survey, choices):
    answer = ''
    table = dict()
    result_type = ['RT', 'CF', 'JM', 'AN']
    # 검사 결과 저장 tabe 
    for i in result_type:
        table[i] = dict()
        table[i][i[0]] = 0
        table[i][i[1]] = 0
    
    # 결과 저장
    for indicator, choice in zip(survey, choices):
        score = choice - 4
        if score < 0:
            table[''.join(sorted(indicator))][indicator[0]] += abs(score)
        elif score > 0:
            table[''.join(sorted(indicator))][indicator[1]] += score
            
    # 결과 산출
    for key, val in table.items():
        if val[key[0]] < val[key[1]]:
            answer += key[1]
        else:
            answer += key[0]
    return answer