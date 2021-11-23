from itertools import product

def match(user, ban):
    if len(user) != len(ban):
        return 0
    
    for i in range(len(user)):
        if ban[i] == '*':
            continue
        if user[i] != ban[i]:
            return 0
    
    return 1

    
def solution(user_id, banned_id):
    answer = 0

    lst = [[] for _ in range(len(banned_id))]
    
    for _, user in enumerate(user_id):
        for i, ban in enumerate(banned_id):
            if match(user, ban):
                lst[i].append(user)

    
    ids = list(product(*lst))
    answers = set()
    
    for id_ in ids:
        if len(id_) == len(set(id_)):
            answers.add(tuple(set(sorted(id_))))

    # print(answers)
    
    return len(answers)
