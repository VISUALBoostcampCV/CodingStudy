from collections import defaultdict
def solution(user_id, banned_id):
    answer = []
    
    ban_dict = defaultdict(list)
    for index_b, b in enumerate(banned_id):
        for index_u, user in enumerate(user_id):
            if len(b) == len(user):
                for i in range(len(b)):
                    if b[i] == '*':
                        continue
                    if b[i] != user[i]:
                        break
                else:
                    ban_dict[index_b].append(index_u)
    stack = [-1]
    def dp(index):
        if len(stack) == len(banned_id)+1:
            s = sorted(stack)
            if s not in answer:
                answer.append(s)
            
        for it in ban_dict[index]:
            if it not in stack:
                stack.append(it)
                dp(index+1)
                
        return stack.pop()
    dp(0)
    return len(answer)

    '''
    테스트 1 〉	통과 (0.02ms, 10.2MB)
    테스트 2 〉	통과 (0.05ms, 10.2MB)
    테스트 3 〉	통과 (0.06ms, 10.2MB)
    테스트 4 〉	통과 (0.04ms, 10.3MB)
    테스트 5 〉	통과 (82.88ms, 10.3MB)
    테스트 6 〉	통과 (1.15ms, 10.3MB)
    테스트 7 〉	통과 (0.04ms, 10.2MB)
    테스트 8 〉	통과 (0.06ms, 10.1MB)
    테스트 9 〉	통과 (0.07ms, 10.2MB)
    테스트 10 〉	통과 (0.04ms, 10.2MB)
    테스트 11 〉	통과 (0.07ms, 10.2MB)
    
    
    '''