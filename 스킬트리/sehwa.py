import re
def solution(skill, skill_trees):
    count = 0
    pattern = "|".join(list(skill))

    for skills in skill_trees:
        temp = "".join(re.findall(pattern,skills))
        skill = skill[:len(temp)]
        if temp == skill:
            count +=1

    return count