from collections import deque
def comparator(a,b):            # 비교
    tmp = 0
    for i,j in zip(a,b):
        if i==j:
            tmp += 1
    if tmp == len(a)-1:
        return True
    return False

def solution(begin, target, words):
    queue = deque([[begin,0]])
    while queue:                # BFS
        w = queue.popleft()
        if w[0] == target:      # 찾으면 바로 return
            return w[1]
        if w[1]>len(words):
            break
        
        for word in words:      # 단어 비교
            if comparator(word,w[0]):
                queue.append([word,w[1]+1])
    return 0