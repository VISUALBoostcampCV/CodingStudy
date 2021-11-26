def solution(line):
    points=[]
    x_points=[]
    y_points=[]
    for i, (a,b,e) in enumerate(line):
        for c,d,f in line[i+1:]:
            if a*d-b*c == 0:
                continue
                
            x=(b*f-e*d)/(a*d-b*c)
            y=(e*c-a*f)/(a*d-b*c)
            if x.is_integer() and y.is_integer():
                points.append([int(x),int(y)])
                x_points.append(int(x))
                y_points.append(int(y))
    answer=[]        
    for i in range(max(y_points)-min(y_points)+1):
        ans=[]
        for j in range(max(x_points)-min(x_points)+1):
            ans.append(".")
        answer.append(ans)
    for x,y in points:
        x=x-min(x_points)
        y=max(y_points) - y
        answer[y][x] = "*"
    a = []
    for line in answer:
        a.append("".join(line))
    return a

'''
테스트 1 〉	통과 (0.35ms, 10.3MB)
테스트 2 〉	통과 (25.82ms, 12.6MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (73.71ms, 15.4MB)
테스트 5 〉	통과 (14.55ms, 11.6MB)
테스트 6 〉	통과 (4.19ms, 10.4MB)
테스트 7 〉	통과 (21.32ms, 12.4MB)
테스트 8 〉	통과 (0.11ms, 10.4MB)
테스트 9 〉	통과 (156.84ms, 10.8MB)
테스트 10 〉	통과 (162.37ms, 10.6MB)
테스트 11 〉	통과 (201.10ms, 10.4MB)
테스트 12 〉	통과 (224.05ms, 10.8MB)
테스트 13 〉	통과 (232.86ms, 11MB)
테스트 14 〉	통과 (204.35ms, 11.2MB)
테스트 15 〉	통과 (198.25ms, 10.4MB)
테스트 16 〉	통과 (179.89ms, 10.3MB)
테스트 17 〉	통과 (207.35ms, 11.4MB)
테스트 18 〉	통과 (199.97ms, 11.3MB)
테스트 19 〉	통과 (220.30ms, 10.4MB)
테스트 20 〉	통과 (151.98ms, 10.3MB)
테스트 21 〉	통과 (176.06ms, 12.1MB)
테스트 22 〉	통과 (0.06ms, 10.3MB)
테스트 23 〉	통과 (0.03ms, 10.3MB)
테스트 24 〉	통과 (0.02ms, 10.3MB)
테스트 25 〉	통과 (0.05ms, 10.3MB)
테스트 26 〉	통과 (0.11ms, 10.3MB)
테스트 27 〉	통과 (0.01ms, 10.3MB)
테스트 28 〉	통과 (0.02ms, 10.2MB)
테스트 29 〉	통과 (0.01ms, 10.4MB)
'''