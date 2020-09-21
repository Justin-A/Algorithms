def solution(array, commands):
    answer = []
    for lst in commands:
        start = lst[0]
        end = lst[1]
        tmp_lst = array[start - 1:end]
        answer.append(sorted(tmp_lst)[lst[2] - 1])
    return answer