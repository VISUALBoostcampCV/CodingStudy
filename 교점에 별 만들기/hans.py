from collections import defaultdict
def solution(line):
    answer = []
    stars = defaultdict(set)
    xs, ys = [], []
    
    for i, (a,b,e) in enumerate(line):
        for c,d,f in line[i+1:]:
            disc = a*d-b*c
            if disc == 0:
                continue
            x = (b*f-e*d)/disc
            y = (e*c-a*f)/disc
            
            if x%1==0 and y%1==0:
                x, y = int(x), int(y)                
                stars[y].add(x)
                print(stars)
                xs.append(x)
                ys.append(y)
                
    len_x = max(xs)-min(xs)+1
    len_y = max(ys)-min(ys)+1
    min_y = min(ys)
    min_x = min(xs)


    print(stars.items())
    for i in reversed(range(len_y)):
        star = ''
        for j in range(len_x):
            if j+min_x in stars[i+min_y]:
                star += '*'
            else:
                star += '.'
        answer.append(star)
    
    return answer

line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
answer = solution(line)
for ans in answer:
    print(ans)


'''
테스트 1 〉	통과 (0.39ms, 10.3MB)
테스트 2 〉	통과 (29.88ms, 11.2MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (67.66ms, 12.1MB)
테스트 5 〉	통과 (17.60ms, 10.8MB)
테스트 6 〉	통과 (5.00ms, 10.4MB)
테스트 7 〉	통과 (25.69ms, 11MB)
테스트 8 〉	통과 (0.14ms, 10.4MB)
테스트 9 〉	통과 (126.74ms, 10.6MB)
테스트 10 〉	통과 (122.69ms, 10.4MB)
테스트 11 〉	통과 (142.25ms, 10.4MB)
테스트 12 〉	통과 (168.60ms, 10.6MB)
테스트 13 〉	통과 (178.17ms, 10.9MB)
테스트 14 〉	통과 (160.01ms, 10.8MB)
테스트 15 〉	통과 (150.72ms, 10.4MB)
테스트 16 〉	통과 (130.48ms, 10.4MB)
테스트 17 〉	통과 (179.41ms, 10.7MB)
테스트 18 〉	통과 (156.90ms, 10.8MB)
테스트 19 〉	통과 (148.23ms, 10.5MB)
테스트 20 〉	통과 (117.77ms, 10.4MB)
테스트 21 〉	통과 (145.42ms, 11MB)
테스트 22 〉	통과 (0.11ms, 10.3MB)
테스트 23 〉	통과 (0.05ms, 10.3MB)
테스트 24 〉	통과 (0.03ms, 10.3MB)
테스트 25 〉	통과 (0.06ms, 10.3MB)
테스트 26 〉	통과 (0.08ms, 10.2MB)
테스트 27 〉	통과 (0.03ms, 10.3MB)
테스트 28 〉	통과 (0.04ms, 10.3MB)
테스트 29 〉	통과 (0.03ms, 10.3MB)

'''