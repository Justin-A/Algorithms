def solution(s):
    words = s.split(" ")
    answer = []
    for word in words:
        x_0 = [val.upper() for idx, val in enumerate(word) if idx % 2 == 0]
        x_1 = [val.lower() for idx, val in enumerate(word) if idx % 2 == 1]
        
        if len(x_0) > len(x_1):
            x_1.append(" ")
        
        value = str()
        for x0, x1 in zip(x_0, x_1):
            value += x0
            value += x1
        answer.append(value)
        
    answer = [x.replace(" ", "") for x in answer]
    answer = ','.join(answer)
    answer = answer.replace(',', ' ')
    return answer