def solution(name, yearning, photo):
    photo_len = len(photo)
    answer = [0] * photo_len
    print(answer)
    score = dict(zip(name, yearning))
    for i in range(photo_len):
        for friend in photo[i]:
            if friend in score:
                answer[i] += score[friend]
    return answer