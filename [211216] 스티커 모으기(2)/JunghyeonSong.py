def solution(sticker):
    # 스티커 길이가 4 미만인 경우
    if len(sticker) < 4:
        return max(sticker)
    
    answer = 0
    index = -1   # 찢어져서 사용할 수 없게 된 스티커 인덱스
    
    # 첫 시작 스티커 체크 (이어진 부분)
    # 첫번째 스티커부터 뗄 경우
    if sticker[0] > sticker[1] + sticker[-1]:
        answer = sticker[0]
        
        # 스티커 찢어짐 처리
        sticker[-1] = 0 
        index = 2
    else:
        sticker[0] = 0
    
    # 스티커 떼기
    while index < len(sticker)-4:
        
        if sticker[index+2] > sticker[index+1] + sticker[index+3]:
            answer += sticker[index+2]
            index = index + 3
        else:
            answer += sticker[index+1]
            index = index + 2
    
    if index > len(sticker) - 4:
        answer += max(sticker[index+1:])
    else:
        answer += max(sticker[index+1]+sticker[index+3], sticker[index+2])
    return answer



'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.4MB)
테스트 2 〉	통과 (0.00ms, 10.4MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	실패 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.4MB)
테스트 7 〉	실패 (0.15ms, 10.2MB)
테스트 8 〉	실패 (0.15ms, 10.3MB)
테스트 9 〉	실패 (0.27ms, 10.2MB)
테스트 10 〉	실패 (0.29ms, 10.2MB)
테스트 11 〉	실패 (0.14ms, 10.2MB)
테스트 12 〉	실패 (0.29ms, 10.4MB)
테스트 13 〉	실패 (0.25ms, 10.4MB)
테스트 14 〉	실패 (0.15ms, 10.4MB)
테스트 15 〉	실패 (0.17ms, 10.2MB)
테스트 16 〉	실패 (0.18ms, 10.4MB)
테스트 17 〉	실패 (0.15ms, 10.3MB)
테스트 18 〉	실패 (0.15ms, 10.3MB)
테스트 19 〉	실패 (0.26ms, 10.3MB)
테스트 20 〉	실패 (0.14ms, 10.3MB)
테스트 21 〉	실패 (0.16ms, 10.2MB)
테스트 22 〉	실패 (0.15ms, 10.2MB)
테스트 23 〉	실패 (0.15ms, 10.3MB)
테스트 24 〉	실패 (0.15ms, 10.2MB)
테스트 25 〉	실패 (0.15ms, 10.3MB)
테스트 26 〉	실패 (0.16ms, 10.2MB)
테스트 27 〉	실패 (0.28ms, 10.4MB)
테스트 28 〉	실패 (0.32ms, 10.1MB)
테스트 29 〉	실패 (0.16ms, 10.2MB)
테스트 30 〉	실패 (0.31ms, 10.2MB)
테스트 31 〉	실패 (0.16ms, 10.4MB)
테스트 32 〉	실패 (0.16ms, 10.2MB)
테스트 33 〉	통과 (0.00ms, 10.2MB)
효율성  테스트
테스트 1 〉	실패 (16.00ms, 10.8MB)
테스트 2 〉	실패 (15.74ms, 10.9MB)
테스트 3 〉	실패 (15.30ms, 10.9MB)
테스트 4 〉	실패 (16.07ms, 10.8MB)
'''