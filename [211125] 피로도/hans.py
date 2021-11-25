from itertools import permutations
def solution(k, d):
    answer = []
    # 던전의 최대길이가 8이므로 완전 탐색 
    for permuted in permutations(d):    
        cnt = 0
        tmp = k
        for need, consume in permuted:
            if tmp < need:
                continue
            tmp-=consume
            cnt+=1
        answer.append(cnt)
    return max(answer)

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.39ms, 10.2MB)
테스트 6 〉	통과 (2.80ms, 10.3MB)
테스트 7 〉	통과 (24.90ms, 10.5MB)
테스트 8 〉	통과 (25.58ms, 10.5MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (2.62ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (26.95ms, 10.4MB)
테스트 13 〉	통과 (19.95ms, 10.4MB)
테스트 14 〉	통과 (19.11ms, 10.5MB)
테스트 15 〉	통과 (31.84ms, 10.4MB)
테스트 16 〉	통과 (2.21ms, 10.3MB)
테스트 17 〉	통과 (19.44ms, 10.5MB)
'''