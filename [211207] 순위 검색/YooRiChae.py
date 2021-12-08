def solution(info, query):
    answer = []
    for q in query:
        a=[]
        split_query = q.replace("and","").split()
        for i in info:
            cnt=0
            split_info = i.split()
            for idx in range(4):
                if split_info[idx] == split_query[idx] or split_query[idx] == "-": cnt+=1
                else: break
            if cnt == 4:
                if int(split_info[-1])>= int(split_query[-1]):
                    a.append(i)
        answer.append(len(a))
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.15ms, 10.3MB)
테스트 2 〉	통과 (0.16ms, 10.4MB)
테스트 3 〉	통과 (2.97ms, 10.4MB)
테스트 4 〉	통과 (20.12ms, 10.5MB)
테스트 5 〉	통과 (60.10ms, 10.5MB)
테스트 6 〉	통과 (153.56ms, 10.5MB)
테스트 7 〉	통과 (61.12ms, 10.6MB)
테스트 8 〉	통과 (314.62ms, 10.7MB)
테스트 9 〉	통과 (345.57ms, 10.6MB)
테스트 10 〉	통과 (375.13ms, 10.7MB)
테스트 11 〉	통과 (62.02ms, 10.5MB)
테스트 12 〉	통과 (152.79ms, 10.5MB)
테스트 13 〉	통과 (69.54ms, 10.6MB)
테스트 14 〉	통과 (441.65ms, 10.5MB)
테스트 15 〉	통과 (361.14ms, 10.5MB)
테스트 16 〉	통과 (100.69ms, 10.5MB)
테스트 17 〉	통과 (180.28ms, 10.5MB)
테스트 18 〉	통과 (388.22ms, 10.6MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
'''