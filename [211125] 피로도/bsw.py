from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    p = list(permutations(dungeons))
    
    # 현재 피로도를 업데이트하며 모든 경우의 수를 탐색
    for dungeon in p:
        now_k = k # 현재 피로도 now_k
        can = 0
        for need, use in dungeon:
            if need <= now_k: 
                now_k -= use
                can += 1
        answer = max(answer, can)
        
    return answer
  
  '''
  정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.06ms, 10.3MB)
테스트 4 〉	통과 (0.08ms, 10.2MB)
테스트 5 〉	통과 (0.48ms, 10.2MB)
테스트 6 〉	통과 (3.56ms, 10.5MB)
테스트 7 〉	통과 (35.44ms, 14.9MB)
테스트 8 〉	통과 (38.04ms, 14.9MB)
테스트 9 〉	통과 (0.06ms, 10.2MB)
테스트 10 〉	통과 (3.37ms, 10.5MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (32.19ms, 14.8MB)
테스트 13 〉	통과 (29.44ms, 14.8MB)
테스트 14 〉	통과 (29.02ms, 14.9MB)
테스트 15 〉	통과 (29.02ms, 14.9MB)
테스트 16 〉	통과 (2.98ms, 10.4MB)
테스트 17 〉	통과 (28.74ms, 14.9MB)
'''
