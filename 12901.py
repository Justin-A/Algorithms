def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    day_after = 0
    for x in range(a - 1):
        day_after += month[x]
    day_after += b
    
    answer = day[(day_after % 7) - 1]
    return answer