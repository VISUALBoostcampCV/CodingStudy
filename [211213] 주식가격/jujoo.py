def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)): # 현재 가격
        for j in range(i + 1, len(prices)): # 다음에 나오는 가격들
            if prices[i] <= prices[j]: # 가격이 떨어지지 않을때
                answer[i] += 1
            else: # 가격이 떨어질때
                answer[i] += 1 # 1초뒤에 가격이 떨어짐
                break
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (1.04ms, 10.3MB)
# 테스트 4 〉	통과 (1.13ms, 10.3MB)
# 테스트 5 〉	통과 (1.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.05ms, 10.2MB)
# 테스트 7 〉	통과 (0.45ms, 10.4MB)
# 테스트 8 〉	통과 (0.50ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.94ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (137.05ms, 18.8MB)
# 테스트 2 〉	통과 (118.64ms, 17.6MB)
# 테스트 3 〉	통과 (187.47ms, 19.5MB)
# 테스트 4 〉	통과 (135.93ms, 18.3MB)
# 테스트 5 〉	통과 (82.95ms, 16.9MB)