def solution(n):
    answer = ''
    num_lst = sorted([x for x in str(n)], reverse = True)
    for num in num_lst:
        answer += num
    return int(answer)