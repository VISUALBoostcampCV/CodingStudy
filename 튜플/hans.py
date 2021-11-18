import re
def solution(s):
    answer = []
    mem = dict()
    s = sorted(re.split('},{',s[2:-2]), key = len)
    # s = sorted(s[2:-2].split('},{'), key=len)
    for item in s:
        # '1,2,3' '2,1' '1,2,4,3'
        item = list(map(int, item.split(',')))
        for j in item:
            if mem.get(j,1):     #j 가 없으면 1을 반환 따라서 j not in mem 과 같다.
            # if j not in mem:
                mem[j] = 0
                answer.append(j)
    return answer


s = solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
print(s)

'''
테스트 1 〉	통과 (0.10ms, 10.4MB)
테스트 2 〉	통과 (0.08ms, 10.4MB)
테스트 3 〉	통과 (0.10ms, 10.4MB)
테스트 4 〉	통과 (0.14ms, 10.4MB)
테스트 5 〉	통과 (0.33ms, 10.3MB)
테스트 6 〉	통과 (0.73ms, 10.3MB)
테스트 7 〉	통과 (5.03ms, 10.5MB)
테스트 8 〉	통과 (13.50ms, 11MB)
테스트 9 〉	통과 (6.35ms, 10.6MB)
테스트 10 〉	통과 (14.80ms, 10.9MB)
테스트 11 〉	통과 (17.99ms, 11.5MB)
테스트 12 〉	통과 (25.41ms, 12.4MB)
테스트 13 〉	통과 (23.90ms, 12.4MB)
테스트 14 〉	통과 (25.47ms, 12.4MB)
테스트 15 〉	통과 (0.10ms, 10.4MB)

'''