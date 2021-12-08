# 효율성 탈락
import pandas as pd
def solution(info, query):
    answer = []
    infos = [i.split() for i in info]
    df = pd.DataFrame(infos, columns=['l', 'j', 'y', 'f', 's'])
    df['s'] = df['s'].astype('int')

    for q in query:
        q, score = q.rsplit(' ', 1)
        score = int(score)
        l, j, y, f = q.split(' and ')
        sub_df = df
        for key, val in [('l', l), ('j', j), ('y', y), ('f', f), ('s', int(score))]:
            if isinstance(val, int):
                answer.append(sum(sub_df[key] >= val))
            if val != '-':
                sub_df = sub_df[sub_df[key] == val]
    return answer

# 효율성 탈락
import re
def solution(info, query):
    answer = []
    infos = []
    for i in info:
        q, score = i.rsplit(' ', 1)
        q = ' and '.join(q.split())
        infos.append((q, int(score)))

    for q in query:
        q, score = q.rsplit(' ', 1)
        q = q.replace('-', '.+')
        answer.append(len(list(filter(lambda x: len(re.findall(q, x[0])) and x[1] >= int(score), infos))))
    return answer

# 효율성 탈락
from collections import defaultdict
def solution(info, query):
    answer = []
    data = defaultdict(list)
                    
    for i in info:
        q, s = i.rsplit(' ', 1)
        l, j, y, f = q.split()
        for a in [l, '-']:
            for b in [j, '-']:
                for c in [y, '-']:
                    for d in [f, '-']:
                        data[(a, b, c, d)].append(((a, b, c, d), int(s)))
    
    for q in query:
        q, s = q.rsplit(' ', 1)
        cnt = 0
        for _, score in data[tuple(q.split(' and '))]:
            if score >= int(s):
                cnt += 1
        answer.append(cnt)
    return answer