import difflib

def solution(begin, target, words):
    answer = []
    visited = [0*i for i in range(len(words))]
    
    def dfs(now,visited):
        for i, w in enumerate(words):
            diff = d.compare(now, w)
            if len(list(diff)) - len(now) == 1 and visited[i]==0:
                visited[i] = 1
                if w == target: 
                    answer.append(visited.count(1))
                else: 
                    dfs(w, visited)
                visited[i] = 0
    
    d = difflib.Differ()
    dfs(begin, visited)
    if not answer: 
        return 0
    return min(answer)

'''
정확성  테스트
테스트 1 〉	통과 (0.12ms, 10.4MB)
테스트 2 〉	통과 (10.93ms, 10.4MB)
테스트 3 〉	통과 (28.37ms, 10.4MB)
테스트 4 〉	통과 (0.29ms, 10.4MB)
테스트 5 〉	통과 (0.05ms, 10.5MB)
'''