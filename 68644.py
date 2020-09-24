# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    sample_lst = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i < j:
                sample_lst.append(numbers[i] + numbers[j])
                
    answer = sorted(list(set(sample_lst)))
    return answer
