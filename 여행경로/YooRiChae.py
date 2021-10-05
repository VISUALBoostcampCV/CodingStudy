def check(arr, place, tickets):
    global t
    arr.append(place)

    for i, (start, end) in enumerate(tickets):
        if start == place:
            tickets.pop(i)
            check(arr, end, tickets)
            tickets.insert(i,[start,end])

    # 모든 도시를 방문하지 않았을 경우 다시 돌아가기
    if len(arr) != t + 1:
        arr.pop()
        
def solution(tickets):
    global t
    t = len(tickets)

    tickets.sort()
    answer = []
    check(answer, "ICN", tickets)
    return answer

'''
테스트 1 〉	통과 (149.28ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
'''