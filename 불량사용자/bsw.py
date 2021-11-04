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
    
    answers = []
    for user in user_id:
        for i, ban in enumerate(banned_id):
            banned_id_list = [0 for _ in range(len(banned_id))]
            if match(user, ban):
                if answers:
                    for ans in answers:
                        if user not in ans and ans[i] == 0:
                            ans[i] = user
                
                banned_id_list[i] = user
                answers.append(banned_id_list)
    
    print(answers)
    s=set()
    for ans in answers:
        if 0 not in ans:
            s.add(tuple(ans))
        
              
        # frodo
        #         frodo
        # fradi
        #         crodo
        #                 abc123
        #                         abc123
        #                 frodoc
        #                         frodoc
        
                
    
    return len(s)
  
  
  '''
  fail
     
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	실패 (0.09ms, 10.3MB)
테스트 3 〉	실패 (0.08ms, 10.3MB)
테스트 4 〉	실패 (0.05ms, 10.2MB)
테스트 5 〉	실패 (0.62ms, 10.2MB)
테스트 6 〉	실패 (0.12ms, 10.2MB)
테스트 7 〉	실패 (0.08ms, 10.3MB)
테스트 8 〉	실패 (0.06ms, 10.2MB)
테스트 9 〉	실패 (0.08ms, 10.3MB)
테스트 10 〉	통과 (0.12ms, 10.3MB)
테스트 11 〉	실패 (0.08ms, 10.3MB)
'''
