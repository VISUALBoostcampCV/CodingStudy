def solution(skill, skill_trees):
    answer = len(skill_trees)
    #선행 스킬 순서
    dic = {}
    for i, v in enumerate(skill):
        dic[v] = i

    for i in range(len(skill_trees)):
        stack = []
        for j in skill_trees[i]:
            if j not in dic: #순서에 없는 시킬시 무시
                continue

            if not stack: #첫 번째
                if dic[j] > 0: #선행 스킬을 배우지않았으면
                    answer -= 1
                    break
            else: #두 번째 이상
                if dic[j] != dic[stack.pop()] + 1:#선행 스킬을 배우지않았으면
                    answer -= 1
                    break
            stack.append(j)
    return answer

"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉통과 (0.01ms, 10.2MB)
테스트 11 〉통과 (0.01ms, 10.2MB)
테스트 12 〉통과 (0.02ms, 10.2MB)
테스트 13 〉통과 (0.01ms, 10.1MB)
테스트 14 〉통과 (0.01ms, 10.2MB)
"""