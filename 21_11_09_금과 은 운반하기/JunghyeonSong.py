from math import ceil   # 올림
from collections import defaultdict
import heapq

def solution(a, b, g, s, w, t):
    answer = 0
    
    # 도시가 하나뿐인 경우
    if len(g) == 1:
        count = ceil((a + b) / w[0]) * 2 - 1    # 총 이동 횟수
        answer = count * t[0]            
        
        return answer
    
    g_time, extra_list = least_time(a, g, w, t)
    
    # 남는 공간 처리
    back = set()
    
    for ei, ew in extra_list:
        # 옮길 자원이 있으면
        if s[ei] > 0:
            # 옮길 자원이 더 있는 경우
            if ew < s[ei]:
                s[ei] -= ew
                b -= ew
                back |= {t[ei]}
            # 자원을 모두 옮긴 경우
            else:
                s[ei] = 0
                b -= s[ei]
    
    back = list(back)
    back = [[b, b] for b in back]
    heapq.heapify(back)
    
    s_time, extra_list = least_time(b, s, w, t, back)
    
    
    answer = max(g_time, s_time)
    
    return answer
    

def least_time(amount, res_list, w_list, t_list, back_heap=[]):
    def _least_time(pre, amount):
        # 돌아와야할 트럭이 있는 경우
        if back_heap:
            # 트럭이 돌아와서 다시 출발하는것보다 더 빠른 시간이 있는 경우
            if time_heap[0] < sum(back_heap[0]):
                # 트럭 출발 처리
                quick_time = heapq.heappop(time_heap)
                
                # todo 광물 리스트 업데이트
                # todo 옮길 광물 남아있으면 돌아올 트럭 업데이트
                heapq.heappush(back_heap, [quick_time, quick_time])
                
                # 돌아오는 트럭 시간 처리
                back_time = heapq.heapop(back_heap)
                b = back_time[0] - quick_time
                
                if b > 0:
                    heapq.heappush(back_heap, [b, back_time[1]])
                else:
                    heapq.heappush(time_heap, back_time[1])
                
            # 트럭이 돌아와서 다시 출발하는게 제일 빠른 경우
            else:
                pass
        # 없는 경우
        else:
            pass
            
        return 0, []
    
    
    # 운반시간 별 인덱스 저장
    time_dict = defaultdict(set)
    
    # 운반 시간 별로 인덱스 및 운반 가능 무게 저장
    for i, (r, w, t) in enumerate(zip(res_list, w_list, t_list)):
        # 옮길 자원이 있는 경우
        if r > 0:
            time_dict[t] |= {i}
    
    # 최소 시간 순으로 정렬
    time_heap = list(time_dict.keys())
    heapq.heapify(time_heap)
    
    # 운반 가능한 도시가 하나인 경우
    if len(time_heap) == 1 and len(time_dict[time_heap[0]]) == 1:
        i = list(time_dict[time_heap[0]])[0]
        count = ceil(amount / w_list[i]) * 2 - 1    # 총 이동 횟수
        time = count * time_heap[0]
        t_amount = count * time_heap[0]
        
        extra = t_amount - amount if t_amount > amount else 0
        extra_list = [[i, extra]]
    else:
        start = 0

        # 목표량 외에 추가로 옮길 수 있는 공간
        extra_list = []
        time, extra_list = _least_time(start, amount)
        
    return time, extra_list