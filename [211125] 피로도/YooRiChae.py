from itertools import permutations

def solution(k, dungeons):

    # 조합에 있는 던전 순서대로 다 탐험할 수 있는지
    def check(now, d_list):
        for m,c in d_list:
            # 못깨면 바로 return 
            if now < m:
                return False
            now -=c
        return True

    answer = -1

    # 몇개의 던전을 탐험할지..
    for n in range(1, len(dungeons)+1):
        # 탐험 순서 가져오기
        dungeons_list = list(permutations(dungeons, n))
        for dungeon in dungeons_list:
            # 조합에 있는 던전 순서대로 다 탐험할 수 있는지 
            if check(k, dungeon):
                answer = n
                # 탐험할 수 있으면 다음 갯수로
                break
                             
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.09ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.53ms, 10.3MB)
테스트 6 〉	통과 (5.79ms, 11.1MB)
테스트 7 〉	통과 (59.87ms, 18.9MB)
테스트 8 〉	통과 (47.05ms, 18.9MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
테스트 10 〉	통과 (6.19ms, 11.1MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (47.36ms, 18.9MB)
테스트 13 〉	통과 (46.67ms, 19MB)
테스트 14 〉	통과 (45.44ms, 19MB)
테스트 15 〉	통과 (49.84ms, 19MB)
테스트 16 〉	통과 (4.48ms, 11.1MB)
테스트 17 〉	통과 (44.48ms, 18.9MB)
'''