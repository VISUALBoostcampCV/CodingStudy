def solution(prices):
    answer = []   
    
    # 가격 떨어지지 않은 기간 계산
    for i, p1 in enumerate(prices):
        count = 0
        for p2 in prices[i+1:]:
            # 1초 카운트
            count += 1
            
            # 떨어졌으면 비교 중지
            if p1 > p2:
                break
                
        # 기간 추가
        answer.append(count)
                
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.79ms, 10.3MB)
테스트 4 〉	통과 (0.96ms, 10.3MB)
테스트 5 〉	통과 (1.32ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.42ms, 10.3MB)
테스트 8 〉	통과 (0.54ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (1.30ms, 10.3MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
'''