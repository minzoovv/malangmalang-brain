def get_balanced_bracket(p):
    count = 0
    for i in range(len(p)):
        if p[i] == ')':
            count += 1
        else:
            count -= 1
        if count == 0:
            return p[0:i+1]


def check_is_perfect_bracket(p):
    count = 0
    if p[0] == ')':
        return False
    else:
        count += 1
        for i in range(1, len(p)):
            if p[i] == '(':
                count += 1
            else:
                count -= 1
        if count == 0:
            return True
        else:
            return False


def make_perfect_bracket(p):
    if len(p) <= 2:
        return ''
    else:
        result_bracket = ''
        for i in range(1, len(p)-1):
            if p[i] == '(':
                result_bracket += ')'
            else:
                result_bracket += '('
        return result_bracket


def solution(p: str):
    if p:
        u, v = get_balanced_bracket(p), p.replace(get_balanced_bracket(p), '', 1)
        if check_is_perfect_bracket(u):
            p = u + solution(v)
        else:
            p = '(' + solution(v) + ')' + make_perfect_bracket(u)
    return p