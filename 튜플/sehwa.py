import re
 
def solution(s):
    answer = []
    a = s.split(',{')
    a.sort(key = len)
    
    for num in a:
        nums = re.findall("\d+", num)
        for i in nums:
            if int(i) not in answer:
                answer.append(int(i))
    return answer


# 테스트 1 〉	통과 (0.09ms, 10.4MB)
# 테스트 2 〉	통과 (0.08ms, 10.4MB)
# 테스트 3 〉	통과 (0.11ms, 10.3MB)
# 테스트 4 〉	통과 (0.11ms, 10.4MB)
# 테스트 5 〉	통과 (0.39ms, 10.4MB)
# 테스트 6 〉	통과 (0.89ms, 10.4MB)
# 테스트 7 〉	통과 (21.35ms, 10.6MB)
# 테스트 8 〉	통과 (111.19ms, 10.9MB)
# 테스트 9 〉	통과 (37.65ms, 10.5MB)
# 테스트 10 〉	통과 (117.02ms, 10.9MB)
# 테스트 11 〉	통과 (168.00ms, 11.2MB)
# 테스트 12 〉	통과 (274.19ms, 11.7MB)
# 테스트 13 〉	통과 (310.54ms, 11.8MB)
# 테스트 14 〉	통과 (315.74ms, 11.7MB)
# 테스트 15 〉	통과 (0.11ms, 10.3MB)