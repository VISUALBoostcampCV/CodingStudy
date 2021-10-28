def solution(skill, skill_trees):
    answer = 0
    
    seq={}
    for i, v in enumerate(skill):
        seq[v] = i
    
    for tree in skill_trees:
        num = -1
        for skl in tree:
            possible = 1
            if not skl in seq:
                continue
            
            if seq[skl] - num == 1:
                num = seq[skl]
            else:
                possible = 0
                break
            
        if possible:
            answer+=1
                
    return answer
