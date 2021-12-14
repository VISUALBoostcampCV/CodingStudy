def solution(prices):
    answer = []   
    
    # 가격 떨어지지 않은 기간 계산
    for i, p1 in enumerate(prices):
        count = 0
        for _i in range(i+1, len(prices)):
            p2 = prices[_i]
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
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.55ms, 10.3MB)
테스트 4 〉	통과 (0.59ms, 10.3MB)
테스트 5 〉	통과 (0.80ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.35ms, 10.3MB)
테스트 8 〉	통과 (0.40ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.76ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (100.72ms, 18.8MB)
테스트 2 〉	통과 (85.96ms, 17.5MB)
테스트 3 〉	통과 (135.89ms, 19.5MB)
테스트 4 〉	통과 (88.88ms, 18.1MB)
테스트 5 〉	통과 (66.30ms, 17.1MB)
'''