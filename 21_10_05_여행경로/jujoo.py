from collections import defaultdict
from typing import List

def solution(tickets:List[List[str]]) -> List[str]:
    '''
    모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
    [Example]
    tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
    return : ["ICN", "COO", "ICN", "BOO", "DOO"]
    '''
    # route : 최종 방문 루트
    # tmp : 방문 가능한 공항을 저장
    route, answer = [], ["ICN"]

    # 방문 가능한 공항을 기준으로 내림차순 정렬
    tickets = sorted(tickets, key=lambda x: x[1], reverse = True)

    # 공항별 방문가능한 공항 저장
    dic = defaultdict(list)
    for start, arrive in tickets:
        dic[start].append(arrive)

    while answer:
        # 방문 공항 경로 저장
        while dic[answer[-1]]:
            answer.append(dic[answer[-1]].pop())
        # 다음 공항이 없을 때 까지 pop
        route.append(answer.pop())
    return route[::-1]