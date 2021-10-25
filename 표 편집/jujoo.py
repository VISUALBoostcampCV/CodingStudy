# < -- 맞왜틀 -- >
# < -- 맞왜틀 -- >
# < -- 맞왜틀 -- >
# < -- 맞왜틀 -- >
# < -- 맞왜틀 -- >
# < -- 맞왜틀 -- >
# < -- 맞왜틀 -- >
def solution(n, k, cmd):
    tbl = list(range(n))
    tmp = []
    cur_idx = k
    for cur_cmd in cmd:
        if cur_cmd == "C":
            tmp.append(tbl.pop(cur_idx))
            if cur_idx > len(tbl) - 1:
                cur_idx = len(tbl) - 1
        elif cur_cmd == "Z":
            prev_data = tmp.pop()
            tbl.insert(prev_data, prev_data)
            if cur_idx > prev_data:
                cur_idx += 1
        else:
            d, cnt = cur_cmd.split()
            if d == "U":
                cur_idx -= int(cnt)
            else:
                cur_idx += int(cnt)
    return ''.join(["O" if i in tbl else "X" for i in range(n)])