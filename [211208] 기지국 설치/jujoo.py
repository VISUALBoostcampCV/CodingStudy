def solution(n, stations, w):
    answer = 0
    width = w * 2 + 1
    prev_loc = 0
    for station in stations:
        left, right = station - w, station + w
        cur_loc = left - prev_loc - 1
        q, r = divmod(cur_loc, width)
        answer += count(q,r)
        if right > n:
            right = n
        prev_loc = right
    if prev_loc < n:
        q, r = divmod(n - prev_loc, width)
        answer += count(q, r)
    return answer

def count(q, r):
    if r:
        return q + 1
    else:
        return q