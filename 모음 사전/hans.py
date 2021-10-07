def solution(word):
    answer = 0
    st = ''
    d1 = {'A':1, 'E':2, 'I':3, 'O':4, 'U':5}
    d2 = {1:'A', 2:'E', 3:'I', 4:'O', 5:'U'}
    while st!=word:
        if len(st)<5:
            st+='A'
        else:
            while st[-1] == 'U':
                st = st[:-1]
            st = st[:-1] + d2[d1[st[-1]]+1]
        # print(st)
        answer += 1
    return answer

print(solution('EIO'))