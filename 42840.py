def solution(answers):
    
    share1, rest1 = divmod(len(answers), 5)
    arr1 = [x for x in range(1, 6)]
    a1 = arr1 * share1 + arr1[:rest1]
    
    share2, rest2 = divmod(len(answers), 8)
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a2 = arr2 * share2 + arr2[:rest2]
    
    share3, rest3 = divmod(len(answers), 10)
    arr3 = [[x] + [x] for x in [3, 1, 2, 4, 5]]
    arr3 = [y for x in arr3 for y in x]
    a3 = arr3 * share3 + arr3[:rest3]
    
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == a1[i]:
            cnt1 += 1
        if answers[i] == a2[i]:
            cnt2 += 1
        if answers[i] == a3[i]:
            cnt3 += 1
    score = {1 : cnt1, 2 : cnt2, 3 : cnt3}
    answer = [key for key in score.keys() if score[key] == max(list(score.values()))]
    return sorted(answer)
