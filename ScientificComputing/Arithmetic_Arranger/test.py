def find_plus_minus(s, l):
    for i in range(l):
        if s[i] == '+' or s[i] == '-':
            return i 
    
    return -1 

def formatter(s, l, ind, show_ans):
    cols = max(ind + 1, l - ind)
    o1 = s[0: ind - 1]
    o2 = s[ind + 1: l]

    ans = ''

    if show_ans:
        res = str(int(o1) + int(o2) if s[ind] == '+' else int(o1) - int(o2))
        ans = ' ' * (cols - len(res)) + res
    
    return [' ' * (cols - ind + 1) + o1, f'{s[ind]}' + ' ' * (cols - l + ind) + o2, '-' * cols, ans] 

def arithmetic_arranger(problems, show_answers=False):
    n = len(problems)
    if n > 5: 
        return 'Error: Too many problems.'
    
    formatted_subs = []
    r = ''

    for i in range(n): 
        l = len(problems[i])
        ind = find_plus_minus(problems[i], l)

        if ind == -1:
            return "Error: Operator must be '+' or '-'."
        elif ind > 5 or l - ind > 6: 
            return "Error: Numbers cannot be more than four digits."
        elif not (problems[i][0: ind - 1].isdigit() and problems[i][ind + 1: l].isdigit()):
            print(problems[i][0: ind - 1].isdigit())
            print(problems[i][ind + 2: l])
            return "Error: Numbers must only contain digits."
        
        a = formatter(problems[i], l, ind, show_answers)
        formatted_subs.append(a)
    
    rows = 4 if show_answers else 3

    for i in range(rows):
        for j in range(n):
            r += formatted_subs[j][i]   
            if j != n - 1: r += '    '
        if i != rows - 1: r += '\n'
    
    return r

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))

zip()