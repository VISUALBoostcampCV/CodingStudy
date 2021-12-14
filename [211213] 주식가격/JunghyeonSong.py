def solution(prices):
    answer = [0 for p in prices]
    is_compare_target = [True for p in prices]  # 비교 대상인지 저장
    
    # 가격 떨어지지 않은 기간 계산
    for compare_end, compare_price in enumerate(prices):
        for index, price in enumerate(prices[:compare_end]):
            # 이미 떨어진 주식이면 넘어감
            if not is_compare_target[index]:
                continue
            
            # 1초 카운트
            answer[index] += 1
            
            # 가격 떨어졌으면 비교 대상에서 제외
            if compare_price < price:
                is_compare_target[index] = False
                
                
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.24ms, 10.3MB)
테스트 3 〉	통과 (11.24ms, 10.3MB)
테스트 4 〉	통과 (15.80ms, 10.3MB)
테스트 5 〉	통과 (21.27ms, 10.3MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (5.81ms, 10.3MB)
테스트 8 〉	통과 (7.86ms, 10.4MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (22.76ms, 10.3MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
'''