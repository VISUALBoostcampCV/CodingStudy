from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    # 던전 탐험 가능한 순서 다 뽑기
    orders = list(permutations(range(len(dungeons)), len(dungeons)))
    
    # 뽑은 순서대로 탐험해보기
    for order in orders:
        hp = k
        count = 0
        
        for o in order:
            # 현재 hp가 최소 필요도보다 적은 경우
            if hp < dungeons[o][0]:
                answer = max(answer, count)
                break
                
            # 탐험 가능한 경우
            count += 1
            hp -= dungeons[o][1]
        else:
            # 모든 던전을 탐험하는 것이 가능한 경우
            answer = len(dungeons)
            break
    
    return answer


'''
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.67ms, 10.3MB)
테스트 6 〉	통과 (4.67ms, 10.4MB)
테스트 7 〉	통과 (42.42ms, 14.8MB)
테스트 8 〉	통과 (48.71ms, 14.9MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (4.47ms, 10.4MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (36.19ms, 14.8MB)
테스트 13 〉	통과 (25.19ms, 14.8MB)
테스트 14 〉	통과 (23.51ms, 14.9MB)
테스트 15 〉	통과 (21.98ms, 14.9MB)
테스트 16 〉	통과 (2.84ms, 10.5MB)
테스트 17 〉	통과 (23.13ms, 14.9MB)
'''