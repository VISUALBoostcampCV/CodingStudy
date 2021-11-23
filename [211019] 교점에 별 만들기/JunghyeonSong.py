from collections import defaultdict

def solution(line):
    answer = []
    
    # 교점 저장할 딕셔너리 {y: {x}}
    cross = defaultdict(set)
    x_min = float('inf')
    x_max = float('-inf')
    
    # 각 직선의 교점 구하기
    for A, B, E in line:
        for C, D, F in line:            
            if A * D - B * C:
                x = (B * F - E * D) / (A * D - B * C)
                y = (E * C - A * F) / (A * D - B * C)

                if x.is_integer() and y.is_integer():
                    x = int(x)
                    y = int(y)
                    cross[y] |= set([x])
                    x_min = min(x, x_min)
                    x_max = max(x, x_max)
                    

    # 별 찍기    
    for y in range(max(cross), min(cross)-1, -1):
        stars = []
        
        # 현재 행에 교점 있으면 stars 리스트에 저장
        if cross[y]:
            stars = sorted(list(cross[y]))
            
        line = ''

        # 교점 없으면 그냥 . 추가
        if not stars:
            answer.append('.' * (x_max - x_min + 1))
            continue
        
        # 이전 교점 위치 저장할 변수
        previous = x_min - 1
        
        # 교점 전까지 . 찍고나서 * 찍기
        for x in stars:
            if x - 1 != previous:
                line += '.' * (x - previous - 1)
            line += '*'
            previous = x
        
        # 교점 이후에 빈공간 있으면 . 찍기
        if previous < x_max:
            line += '.' * (x_max - previous)
                
        answer.append(line)    
        
    return answer


    '''
    테스트 1 〉	통과 (0.16ms, 10.3MB)
    테스트 2 〉	통과 (1.22ms, 11.2MB)
    테스트 3 〉	통과 (0.15ms, 10.4MB)
    테스트 4 〉	통과 (0.77ms, 12.1MB)
    테스트 5 〉	통과 (0.62ms, 10.8MB)
    테스트 6 〉	통과 (0.36ms, 10.4MB)
    테스트 7 〉	통과 (0.53ms, 10.9MB)
    테스트 8 〉	통과 (0.09ms, 10.3MB)
    테스트 9 〉	통과 (300.13ms, 10.7MB)
    테스트 10 〉	통과 (337.77ms, 10.4MB)
    테스트 11 〉	통과 (365.70ms, 10.4MB)
    테스트 12 〉	통과 (424.62ms, 10.6MB)
    테스트 13 〉	통과 (442.61ms, 10.9MB)
    테스트 14 〉	통과 (377.56ms, 10.8MB)
    테스트 15 〉	통과 (380.87ms, 10.4MB)
    테스트 16 〉	통과 (353.08ms, 10.3MB)
    테스트 17 〉	통과 (379.35ms, 10.6MB)
    테스트 18 〉	통과 (368.52ms, 10.9MB)
    테스트 19 〉	통과 (396.37ms, 10.5MB)
    테스트 20 〉	통과 (295.15ms, 10.4MB)
    테스트 21 〉	통과 (297.99ms, 11MB)
    테스트 22 〉	통과 (0.10ms, 10.3MB)
    테스트 23 〉	통과 (0.06ms, 10.3MB)
    테스트 24 〉	통과 (0.03ms, 10.3MB)
    테스트 25 〉	통과 (0.08ms, 10.3MB)
    테스트 26 〉	통과 (0.12ms, 10.3MB)
    테스트 27 〉	통과 (0.02ms, 10.3MB)
    테스트 28 〉	통과 (0.03ms, 10.3MB)
    테스트 29 〉	통과 (0.02ms, 10.3MB)
    '''