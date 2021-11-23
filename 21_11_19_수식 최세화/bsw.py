from itertools import permutations

def solution(expression):
    answer = 0
    
    ops = []
    nums = []
    j=0
    for i, c in enumerate(expression):
        if not c.isdigit():
            nums.append(int(expression[j:i]))
            ops.append(c)
            j=i+1
    nums.append(int(expression[j:]))
    
    priorities = list(permutations(set(ops)))
    
    for priority in priorities:
        calulate(nums, ops, priority)
    
    return answer


def cal(n1, n2, op):
    if op == "+":
        return n1+n2
    elif op == "-":
        return n1-n2:
    elif op == "*":
        return n1*n2
     

def calulate(nums, ops, prior):
    for p in prior:
        for i, op in enumerate(ops):
            if op == p:
                nums[i] = cal(nums[i], nums[i+1], op)
                pass

        
        
