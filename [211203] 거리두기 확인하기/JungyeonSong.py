from collections import deque

def solution(places):
    answer = []
    
    def look_around(i, j):
        # 맨해튼 거리 1
        space1 = {'u':(-1, 0), 'd':(1, 0), 'l':(0, -1), 'r':(0, 1)}
        space2 = [((-1, -1), ('u', 'l')), ((-1, 1), ('u', 'r')),
                  ((1, -1), ('d', 'l')), ((1, 1), ('d', 'r')),
                  ((-2, 0), 'u'), ((2, 0), 'd'), ((0, -2), 'l'), ((0, 2), 'r')]
        
        # 맨헤튼 거리 1 체크
        for index in space1.values():
            _i = i + index[0]
            _j = j + index[1]
            
            # 인덱스 범위 벗어나는 경우
            if _i < 0 or _i > 4 or _j < 0 or _j > 4:
                continue
            
            # 사람 있는 경우
            if place[_i][_j] == 'P':
                return 0
            
        # 맨헤튼 거리 2 체크
        for index, direction in space2:
            _i = i + index[0]
            _j = j + index[1]
            
            # 인덱스 범위 벗어나는 경우
            if _i < 0 or _i > 4 or _j < 0 or _j > 4:
                continue
            
            # 사람 있는경우
            if place[_i][_j] == 'P':
                x_count = 0
                
                for d in direction:
                    index = space1[d]
                    _i = i + index[0]
                    _j = j + index[1]
                    
                    if place[_i][_j] == 'X':
                        x_count += 1
                
                if x_count < len(direction):
                    return 0
        
        return 1
            
    
    # 5개 대기실 체크
    for place in places:
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and not look_around(i, j):
                    answer.append(0)
                    i = 5
                    break
            if i == 5:
                break
        else:
            answer.append(1)
                
            
        
    return answer


'''
테스트 1 〉	통과 (0.11ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.06ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.06ms, 10.3MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.4MB)
테스트 12 〉	통과 (0.03ms, 10.4MB)
테스트 13 〉	통과 (0.03ms, 10.4MB)
테스트 14 〉	통과 (0.04ms, 10.3MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
테스트 16 〉	통과 (0.04ms, 10.3MB)
테스트 17 〉	통과 (0.04ms, 10.3MB)
테스트 18 〉	통과 (0.03ms, 10.3MB)
테스트 19 〉	통과 (0.04ms, 10.3MB)
테스트 20 〉	통과 (0.05ms, 10.4MB)
테스트 21 〉	통과 (0.04ms, 10.3MB)
테스트 22 〉	통과 (0.05ms, 10.3MB)
테스트 23 〉	통과 (0.02ms, 10.3MB)
테스트 24 〉	통과 (0.01ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.3MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
테스트 27 〉	통과 (0.04ms, 10.3MB)
테스트 28 〉	통과 (0.05ms, 10.3MB)
테스트 29 〉	통과 (0.06ms, 10.3MB)
테스트 30 〉	통과 (0.03ms, 10.3MB)
'''