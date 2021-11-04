def depth(temp_ban, ban_users,result, idx):
    for user in temp_ban[idx]:
        ban_users.append(user)

        if idx == len(temp_ban)-1:
            if len(set(ban_users)) != len(temp_ban): pass
            elif set(ban_users) in result: pass
            else:
                result.append(set(ban_users))
            ban_users.pop()
            
        else:
            depth(temp_ban,ban_users,result, idx+1)
            ban_users.pop()
        
def check(user, ban):
    for i in range(0, len(user)):
        if ban[i] == "*": 
            continue
        elif user[i] != ban[i]:
            return 0
    return 1

def solution(user_id, banned_id):
    #  불량 사용자 아이디에서 일치하는 아이디 구하기
    temp_ban=[[] for i in range(0, len(banned_id))]    
    for i, ban in enumerate(banned_id):
        for user in user_id:
            if len(ban) == len(user):
                if check(user, ban):
                    temp_ban[i].append(user)
                    
    result = []
    ban_users = []
    
    # 경우의 수
    depth(temp_ban, ban_users, result, 0)
    
    return len(result)

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.08ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (7414.70ms, 10.4MB)
테스트 6 〉	통과 (2.55ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.05ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.3MB)
테스트 11 〉	통과 (0.06ms, 10.3MB)
'''