import re
def solution(skill, skill_trees):
    count = 0
    pattern = "|".join(list(skill))
    for skills in skill_trees:
        temp = "".join(re.findall(pattern,skills))
        if temp == "":
            count +=1
            continue
        skill_p= skill[:len(temp)]
        if temp == skill_p:
            count +=1
    return count


# 테스트 1 〉	통과 (0.07ms, 10.3MB)
# 테스트 2 〉	통과 (0.08ms, 10.2MB)
# 테스트 3 〉	통과 (0.09ms, 10.2MB)
# 테스트 4 〉	통과 (0.12ms, 10.2MB)
# 테스트 5 〉	통과 (0.10ms, 10.2MB)
# 테스트 6 〉	통과 (0.08ms, 10.1MB)
# 테스트 7 〉	통과 (0.10ms, 10.3MB)
# 테스트 8 〉	통과 (0.14ms, 10.2MB)
# 테스트 9 〉	통과 (0.11ms, 10.2MB)
# 테스트 10 〉	통과 (0.10ms, 10.2MB)
# 테스트 11 〉	통과 (0.10ms, 10.2MB)
# 테스트 12 〉	통과 (0.16ms, 10.2MB)
# 테스트 13 〉	통과 (0.10ms, 10.2MB)
# 테스트 14 〉	통과 (0.05ms, 10.2MB)