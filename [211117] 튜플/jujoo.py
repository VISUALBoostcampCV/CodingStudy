import re
def solution(s):
    answer = []
    # 중괄호 안에 숫자와 ,로 이루어진 문자만 추출
    sub_list = re.findall('{[\d,]+}', s[1:-1])
    # 길이가 작은 순서로 추가
    for sub_tuple in sorted(sub_list, key=lambda x : len(x)):
        for num in list(map(lambda x : int(x), sub_tuple[1:-1].split(','))):
            if num not in answer:
                answer.append(num)
    return answer

# 테스트 1 〉	통과 (0.11ms, 10.4MB)
# 테스트 2 〉	통과 (0.14ms, 10.4MB)
# 테스트 3 〉	통과 (0.12ms, 10.4MB)
# 테스트 4 〉	통과 (0.14ms, 10.3MB)
# 테스트 5 〉	통과 (0.59ms, 10.4MB)
# 테스트 6 〉	통과 (1.18ms, 10.4MB)
# 테스트 7 〉	통과 (34.08ms, 10.5MB)
# 테스트 8 〉	통과 (100.77ms, 11.1MB)
# 테스트 9 〉	통과 (34.24ms, 10.6MB)
# 테스트 10 〉	통과 (190.46ms, 11.1MB)
# 테스트 11 〉	통과 (167.71ms, 11.5MB)
# 테스트 12 〉	통과 (369.56ms, 12.4MB)
# 테스트 13 〉	통과 (264.49ms, 12.1MB)
# 테스트 14 〉	통과 (281.38ms, 12.2MB)
# 테스트 15 〉	통과 (0.10ms, 10.5MB)