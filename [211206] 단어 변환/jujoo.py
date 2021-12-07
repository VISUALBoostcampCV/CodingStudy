def solution(begin, target, words):
    answer = []
    stack = [begin]
    if target not in words:
        return 0
    def dfs(begin, words):
        # 이미 이전에 나온 최소 길이보다 길어지면 가지치기를 해버림
        if len(answer) and len(stack) > min(answer):
            return
        # target에 도달하면 현재까지의 길이를 추가
        if stack[-1] == target:
            answer.append(len(stack))
            return
        for word in words:
            # 이미 변환한 word면 pss
            if word in stack:
                continue
            # 하나의 문자만 다르면 cnt = 1이 된다
            cnt = 0
            for left, right in zip(word, begin):
                if left != right:
                    cnt += 1
            # cnt가 1일때만 stack에 추가하고 이후 dfs 실행
            if cnt == 1:
                stack.append(word)
                dfs(word, words)
                # target에 도달하거나 for문이 다 돌았다거나 가지치기가 되었을때 마지막 값을 pop()
                stack.pop()
    dfs(begin, words)
    return min(answer) - 1