def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        tree = list(reversed(skill))
        t = tree.pop()
        for s in sk:
            if s in tree:
                break
            elif s==t:
                t=tree.pop() if tree else t
        else:
            answer += 1
            
    return answer