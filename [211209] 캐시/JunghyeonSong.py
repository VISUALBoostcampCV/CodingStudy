def solution(cacheSize, cities):
    answer = 0
    
    # 캐시 사이즈 0이면
    if not cacheSize:
        return len(cities) * 5
    
    # 캐시
    cache = []
    
    # 캐시 실행시간 측정
    for city in cities:
        city = city.lower() # 대소문자 구분 없애기

        # 캐시에 해당 도시가 이미 있는 경우
        if city in cache:
            answer += 1
            cache.remove(city)
        # 캐시에 해당 도시가 없는 경우
        else:
            answer += 5
            # 이미 캐시 꽉찼으면
            if len(cache) == cacheSize:
                cache = cache[1:]   # 제일 오래된 애 삭제
        cache.append(city)  # 제일 최근 도시 맨 뒤로
            
    return answer


    '''
    정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (69.61ms, 17.7MB)
테스트 12 〉	통과 (0.05ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.2MB)
테스트 14 〉	통과 (0.10ms, 10.3MB)
테스트 15 〉	통과 (0.15ms, 10.3MB)
테스트 16 〉	통과 (0.18ms, 10.3MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.42ms, 10.3MB)
테스트 19 〉	통과 (0.54ms, 10.2MB)
테스트 20 〉	통과 (0.70ms, 10.3MB)
    '''