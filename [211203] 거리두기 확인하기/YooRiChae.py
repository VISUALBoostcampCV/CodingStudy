def solution(places):
    def manhattan(T1, T2):
        return abs(T1[0]-T2[0]) + abs(T1[1]-T2[1])
    
    def find_P(P):
        if p.find('P')!=-1:
            for i, s in enumerate(p): 
                if s == 'P': P.append ([row,i])
    
    answer = []
    for place in places:
        P=[] # 사람이 앉아있는 좌표
        flag = 0
        
        for row, p in enumerate(place):
            find_P(P)
                               
        for i, p1 in enumerate(P):
            for p2 in P[i+1:]:
                dist = manhattan(p1,p2) # 두 사람의 맨해튼 거리
                if dist < 2: # 옆에 앉아있을 경우
                    answer.append(0)
                    flag = 1
                    break
                elif dist == 2:
                    if (p1[0]==p2[0])or(p1[1]==p2[1]): # 일직선으로 앉아있는 경우
                        x, y = [(p1[0]+p2[0])//2, (p1[1]+p2[1])//2]
                        if place[x][y] != 'X':  # 가운데 좌석이 파티션이 아닐 경우 
                            answer.append(0)
                            flag = 1
                            break 
                    else:   # 대각선으로 앉아있는 경우 
                        if place[p1[0]][p2[1]] == 'O' or place[p2[0]][p1[1]] == 'O': # 사이에 빈 테이블이 있을 경우
                            answer.append(0)
                            flag = 1
                            break 
            if flag: break
        if not flag:               
            answer.append(1)
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.03ms, 10.4MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 10.4MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.03ms, 10.3MB)
테스트 18 〉	통과 (0.03ms, 10.3MB)
테스트 19 〉	통과 (0.03ms, 10.3MB)
테스트 20 〉	통과 (0.04ms, 10.3MB)
테스트 21 〉	통과 (0.04ms, 10.3MB)
테스트 22 〉	통과 (0.03ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (0.04ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.3MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
테스트 27 〉	통과 (0.03ms, 10.3MB)
테스트 28 〉	통과 (0.03ms, 10.3MB)
테스트 29 〉	통과 (0.02ms, 10.3MB)
테스트 30 〉	통과 (0.03ms, 10.3MB)
'''