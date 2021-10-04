from collections import defaultdict, deque
def solution(tickets):
    answer = ["ICN"]
    d = defaultdict(deque)
    tickets.sort()
    
    for t in tickets:
        d[t[0]].append(t[1])
    
    while len(answer) <= len(tickets):
        if not d[answer[-1]]:
            d[answer[-2]].append(answer[-1])
            answer.pop()
        else:
            answer.append(d[answer[-1]].popleft())
            
    return answer