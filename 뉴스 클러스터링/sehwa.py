def input_str(raw_str):
    '''
    자카드 유사도를 측정하기 위해, 갈무리된 형태로 변형
    '''
    str = []
    for index in range(len(raw_str)-1):
        raw_str = raw_str.lower()
        if raw_str[index:index+2].isalpha():
            str.append(raw_str[index:index+2])
            
    return str


def jaccard_similarity(str1, str2):
    '''
    자카드 유사도 판별
    '''
    if not str1 and not str2 :
        return 1

    intersec = str1+str2
    union = str1+str2
    for char in str1 :
        if char in str2:
            union.remove(char)
            str2.remove(char)
            
    intersec = len(intersec) - len(union)
        
    return intersec / len(union)


def solution(str1, str2):
    
    answer = int(jaccard_similarity(input_str(str1), input_str(str2)) * 65536)
        
    return answer



# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (1.99ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.08ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.07ms, 10.3MB)
# 테스트 10 〉	통과 (0.17ms, 10.4MB)
# 테스트 11 〉	통과 (0.34ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.07ms, 10.3MB)