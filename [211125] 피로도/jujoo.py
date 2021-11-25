from itertools import permutations as pm
def solution(k, dungeons):
    answer = -1
    # 모든 순열을 확인
    for dungeon in pm(dungeons, len(dungeons)):
        cur_k = k
        cur_cnt = 0
        # 현재 순열 확인
        for min_fatigue, reduce_fatigue in dungeon:
            # 피로도가 될때까지 던돌
            if cur_k >= min_fatigue:
                cur_k -= reduce_fatigue
                cur_cnt += 1
            # 피로도가 없으면 break
            if cur_k < 0:
                break
        answer = max(answer, cur_cnt)
    return answer