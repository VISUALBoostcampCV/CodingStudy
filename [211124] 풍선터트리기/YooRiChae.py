def solution(a):
    answer = [0]*len(a)
    left = float('inf')
    right = float('inf')
    
    # 오른쪽에 있는 번호가 더 작은 풍선이 있어는 경우
    # 왼쪽에는 무조건 더 큰 풍선이 있어야됨
    for i in range(len(a)):
        if left > a[i]:
            left = a[i]
            answer[i] = 1
            
    # 왼쪽에 있는 번호가 더 작은 풍선이 있어는 경우
    # 오른쪽에는 무조건 더 큰 풍선이 있어야됨            
    for j in range(len(a)-1, -1, -1):
        if right > a[j]:
            right = a[j]
            answer[j] = 1
            
    return sum(answer)