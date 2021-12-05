from collections import defaultdict, deque

def solution(begin, target, words):
    answer = 0
    
    # 변환할 수 없는 경우
    if target not in words:
        return answer
    
    word_tree = defaultdict(list)
    total = [begin] + words
    index = dict(zip(total, range(len(total))))
    
    # 탐색할 트리 구성
    for word1 in total:
        for word2 in total:
            if word1 is word2:
                continue
            if count_diff(word1, word2) == 1:
                word_tree[word1].append(word2)
    
    # 탐색 시작
    queue = deque([begin])
    count = [0 for t in total]
    count[index[begin]] = 1
        
    while queue:
        word = queue.popleft()

        for w in word_tree[word]:
            # 처음 체크한 단어면
            if not count[index[w]]:
                count[index[w]] = count[index[word]] + 1
                queue.append(w)
            
    answer = count[index[target]]-1
    
    return answer


# 몇개 알파벳이 다른지 세주는 함수
def count_diff(word1, word2):
    count = 0
    
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            count += 1
            
    return count



'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.53ms, 10.3MB)
테스트 3 〉	통과 (1.86ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.4MB)
'''