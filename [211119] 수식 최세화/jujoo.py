import re
from itertools import permutations

def solution(expression):
	#expression 안에 있는 연산자들을 저장
    operators = [operator for operator in ['*','+','-'] if operator in expression]
    nums = re.split(r'(\D)',expression)

    answer = []
    for cur_operators in permutations(operators):
        _nums = nums[:]
        for operator in cur_operators:
            while operator in _nums:
                idx = _nums.index(operator)
                _nums[idx - 1] = str(eval(_nums[idx - 1] + _nums[idx] + _nums[idx + 1]))
                _nums = _nums[:idx] + _nums[idx + 2:]

        answer.append(_nums.pop())

    return max(abs(int(n)) for n in answer)