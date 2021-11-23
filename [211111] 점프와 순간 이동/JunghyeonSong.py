def solution(n):
    way_dict = {1: 1, 2: 1}
    ans = jump_or_teleport(n, way_dict)

    return ans


def jump_or_teleport(n, way_dict):
    if way_dict.get(n):
        return way_dict[n]    

    # 홀수인 경우
    if n % 2:
        way_dict[n] = jump_or_teleport(n-1, way_dict) + 1    
    # 짝수인 경우
    else:
        way_dict[n] = jump_or_teleport(n//2, way_dict)    

    return way_dict[n]


'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)

효율성  테스트
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 9.92MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (0.03ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 9.98MB)
테스트 8 〉	통과 (0.01ms, 9.97MB)
테스트 9 〉	통과 (0.02ms, 9.93MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
'''