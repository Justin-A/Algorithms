def solution(strings, n):
    str_dic = {idx : x[n] for idx, x in enumerate(strings)}
    sorted_lst = sorted(list(str_dic.values()))
    
    tmp = []
    for x in sorted_lst:
        tmp.append(sorted([strings[key] for key, value in str_dic.items() if value == x]))    
        
    tmp = [y for x in tmp for y in x]
    
    answer = []
    for x in tmp:
        if x not in answer:
            answer.append(x)
    
    return answer