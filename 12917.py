def solution(s):
    lower = sorted([x for x in s if x.islower()], reverse = True)
    upper = sorted([x for x in s if x.isupper()], reverse = True)
    
    lower = ','.join(lower)
    upper = ','.join(upper)
    
    lower = str(lower).replace(",", "")
    upper = str(upper).replace(",", "")
    
    return lower + upper