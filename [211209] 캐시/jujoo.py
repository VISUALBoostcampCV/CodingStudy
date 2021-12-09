from collections import deque
def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * 5
    
    time = 0 # 걸린 시간
    cache = [] # 캐시
    cities = deque(cities) # 도시
    
    while cities:
        cur_city = cities.popleft().lower() # 소문자 통일
        # 캐시가 비어있거나 현재 도시가 캐시에 없으면 miss
        if not cache or cur_city not in cache:
            if len(cache) == cacheSize:
                cache.pop(0) # 가장 오래된 캐시 삭제(n)
            cache.append(cur_city)
            time += 5
        else:
            # 현재 사용한 캐시를 맨 뒤로 이동(n^2)
            cache.append(cache.pop(cache.index(cur_city)))
            time += 1
            
    return time

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.4MB)
# 테스트 10 〉	통과 (0.04ms, 10.4MB)
# 테스트 11 〉	통과 (77.88ms, 17.7MB)
# 테스트 12 〉	통과 (0.04ms, 10.4MB)
# 테스트 13 〉	통과 (0.07ms, 10.3MB)
# 테스트 14 〉	통과 (0.10ms, 10.4MB)
# 테스트 15 〉	통과 (0.26ms, 10.3MB)
# 테스트 16 〉	통과 (0.27ms, 10.3MB)
# 테스트 17 〉	통과 (0.00ms, 10.4MB)
# 테스트 18 〉	통과 (0.42ms, 10.2MB)
# 테스트 19 〉	통과 (0.58ms, 10.2MB)
# 테스트 20 〉	통과 (0.66ms, 10.3MB)