def chg_str(strr):
    lower = ''
    for s in strr:
        if s.isupper():
            s = s.lower()
        lower += s
    return lower


def cut_str_lst(lower_str):
    str_lst = []
    
    for i in range(len(lower_str)-1):
        cut = lower_str[i:i+2]
        if not cut.isalpha():
            continue
        str_lst.append(cut)
    
    return str_lst


def jaccard_num(lst1, lst2):
    if not lst1 and not lst2:
        return 65536
    
    set1 = set(lst1+lst2)
    inter = 0
    for s in set1:
        cnt_inlst1 = lst1.count(s)
        cnt_inlst2 = lst2.count(s)
        inter += min(cnt_inlst1, cnt_inlst2)
            
    union = len(lst1)+len(lst2)-inter
    return int(inter/union * 65536)
    
    

def solution(str1, str2):

    lst1 = cut_str_lst(chg_str(str1))
    lst2 = cut_str_lst(chg_str(str2))    
    
    return jaccard_num(lst1, lst2)