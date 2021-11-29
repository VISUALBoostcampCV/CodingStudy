from itertools import permutations

def solution(k, dungeons):
    answer = -1
    route = list(permutations(dungeons))

    for r in route:
        temp = k
        count = 0
        for least, waste in r:
            if least <= temp: 
                count += 1
                temp -= waste
            else :
                break
        answer = max(answer, count)
        
    return answer


# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.08ms, 10.2MB)
# 테스트 4 〉	통과 (0.13ms, 10.2MB)
# 테스트 5 〉	통과 (0.49ms, 10.3MB)
# 테스트 6 〉	통과 (3.37ms, 10.5MB)
# 테스트 7 〉	통과 (40.23ms, 14.9MB)
# 테스트 8 〉	통과 (64.30ms, 14.9MB)
# 테스트 9 〉	통과 (0.07ms, 10.2MB)
# 테스트 10 〉	통과 (3.62ms, 10.4MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (41.25ms, 14.8MB)
# 테스트 13 〉	통과 (21.81ms, 14.9MB)
# 테스트 14 〉	통과 (22.03ms, 14.8MB)
# 테스트 15 〉	통과 (20.67ms, 14.9MB)
# 테스트 16 〉	통과 (2.06ms, 10.5MB)
# 테스트 17 〉	통과 (21.76ms, 14.9MB)
