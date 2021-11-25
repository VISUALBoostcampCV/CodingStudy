import sys
# O(3n)
def solution(a):
    #풍선이 하나 밖에 없을때 예외처리
    if len(a) == 1:
        return 1
    
    answer = 0
    left = right = sys.maxsize #가장 큰 값을 default로 지정
    #왼쪽과 오른쪽에서 살아남는 풍선을 저장
    arr = [[0] * len(a) for _ in range(2)]
    
    #왼쪽 0부터 마지막 인덱스까지 이동하면서 살아남는 풍선을 저장
    for i in range(len(a)):
        if left > a[i]:
            left = a[i]
        arr[0][i] = left
        
    #왼쪽과 반대로 오른쪽 마지막인덱스부터 0까지 이동하면서 살아남는 풍선을 저장
    for i in reversed(range(len(a))):
        if right > a[i]:
            right = a[i]
        arr[1][i] = right
        
    #해당 풍선의 오른쪽(arr[0]) 또는 왼쪽(arr[1]) 중 한 쪽이라도 더 크거나 같으면 해당 풍선은 살아남는다
    #왜냐하면 더 작은 풍선을 터뜨리는 행위를 하게되면 한 쪽이 더 작더라도 살아남기 때문이다
    for i in range(len(a)):
        if a[i] <= arr[0][i] or a[i] <= arr[1][i]:
            answer += 1
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.30ms, 10.2MB)
# 테스트 4 〉	통과 (31.75ms, 15.3MB)
# 테스트 5 〉	통과 (180.35ms, 36.9MB)
# 테스트 6 〉	통과 (229.82ms, 50.3MB)
# 테스트 7 〉	통과 (337.69ms, 63.9MB)
# 테스트 8 〉	통과 (351.46ms, 64MB)
# 테스트 9 〉	통과 (336.61ms, 64MB)
# 테스트 10 〉	통과 (326.35ms, 63.9MB)
# 테스트 11 〉	통과 (363.39ms, 63.9MB)
# 테스트 12 〉	통과 (366.69ms, 64MB)
# 테스트 13 〉	통과 (336.22ms, 63.9MB)
# 테스트 14 〉	통과 (306.55ms, 64MB)
# 테스트 15 〉	통과 (306.95ms, 64MB)