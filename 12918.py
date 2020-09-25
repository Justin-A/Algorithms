def solution(s):
    if (len(s) == 4) or (len(s) == 6):
        answer = [False if x.isalpha() else True for x in s]
        return all(answer)
    else:
        return False