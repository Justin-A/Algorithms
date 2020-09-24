def solution(s, n):
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
    ALPHA = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
    
    answer = ''
    for x in s:
        if x in alpha:
            return_x = alpha[(alpha.index(x) + n) % len(alpha)]
        elif x in ALPHA:
            return_x = ALPHA[(ALPHA.index(x) + n) % len(ALPHA)]
        else:
            return_x = " "
        answer += return_x
        
    return answer