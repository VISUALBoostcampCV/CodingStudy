def search(p):
    move = [(0,1),(0,-1),(1,0),(-1,0)]  # 우, 좌, 하, 상
    for y in range(5):
        for x in range(5):
            if p[y][x]=='P':
                for my, mx in move:
                    new_y, new_x = y+my,x+mx
                    if new_y<0 or new_x<0 or new_y>=5 or new_x>=5:
                        continue
                    if p[new_y][new_x]=='P':
                        return 0
            elif p[y][x]=='O':
                cnt = 0
                for my, mx in move:
                    new_y, new_x = y+my,x+mx
                    if new_y<0 or new_x<0 or new_y>=5 or new_x>=5:
                        continue
                    if p[new_y][new_x]=='P':
                        cnt+=1
                if cnt>=2:
                    return 0
    return 1
                        
                        

def solution(places):
    answer = []
    
    for place in places:
        answer.append(search(place))
    return answer

'''
테스트 1 〉	통과 (0.07ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.07ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 10.3MB)
테스트 14 〉	통과 (0.06ms, 10.4MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
테스트 16 〉	통과 (0.06ms, 10.3MB)
테스트 17 〉	통과 (0.05ms, 10.3MB)
테스트 18 〉	통과 (0.04ms, 10.3MB)
테스트 19 〉	통과 (0.03ms, 10.3MB)
테스트 20 〉	통과 (0.05ms, 10.2MB)
테스트 21 〉	통과 (0.02ms, 10.3MB)
테스트 22 〉	통과 (0.03ms, 10.3MB)
테스트 23 〉	통과 (0.03ms, 10.3MB)
테스트 24 〉	통과 (0.01ms, 10.3MB)
테스트 25 〉	통과 (0.11ms, 10.3MB)
테스트 26 〉	통과 (0.04ms, 10.3MB)
테스트 27 〉	통과 (0.03ms, 10.3MB)
테스트 28 〉	통과 (0.05ms, 10.4MB)
테스트 29 〉	통과 (0.07ms, 10.3MB)
테스트 30 〉	통과 (0.05ms, 10.3MB)

'''