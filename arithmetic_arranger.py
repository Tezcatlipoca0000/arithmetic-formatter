def arithmetic_arranger(problems, solved=False):
    arranged_problems = ''''''
    op1 = []
    op2 = []
    op3 = []
    solutions = []
    #print('the argument:', problems)

    # Rule 1: No more than 5 problems
    length = len(problems)
    #print('Amount of problems:', length)
    if length > 5 : 
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems
    
    for problem in problems :
        splited = problem.split()

        # Rule 2: Only + or -
        if '+' not in splited[1] and '-' not in splited[1] :
            arranged_problems = "Error: Operator must be '+' or '-'."
            break
        
        # Rule 3: Only integers
        if not splited[0].isdigit() or not splited[2].isdigit():
            arranged_problems = 'Error: Numbers must only contain digits.'
            break

        # Rule 4: each operand has a max of 4 digits
        if len(splited[0]) > 4 or len(splited[2]) > 4 :
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
            break
        
        # Solving the problems
        if solved :
            if splited[1] == '+' :
                solutions.append(int(splited[0]) + int(splited[2]))
            else :
                solutions.append(int(splited[0]) - int(splited[2]))

        # sorting 
        op1.append(splited[0])
        op3.append(splited[1])
        op2.append(splited[2])
    
    # Exit on error
    if 'Error' in arranged_problems :
        return arranged_problems

    # Line 1
    for i in range(len(op1)) :
        max_len = max([len(op1[i]), len(op2[i])]) + 2
        for j in range(max_len - len(op1[i])) :
            arranged_problems = arranged_problems + ' '
        arranged_problems = arranged_problems + op1[i]
        if i + 1 < len(op1) :
            arranged_problems = arranged_problems + '    '
        else :
            arranged_problems = arranged_problems + '\n'

    # Line 2
    for i in range(len(op2)) :
        max_len = max([len(op1[i]), len(op2[i])]) + 1
        arranged_problems = arranged_problems + op3[i]
        for j in range(max_len - len(op2[i])) :
            arranged_problems = arranged_problems + ' '
        arranged_problems = arranged_problems + op2[i]
        if i + 1 < len(op2) :
            arranged_problems = arranged_problems + '    '
        else :
            arranged_problems = arranged_problems + '\n'

    # Line 3
    for i in range(len(op3)) :
        max_len = max([len(op1[i]), len(op2[i])]) + 2
        for j in range(max_len) :
            arranged_problems = arranged_problems + '-'
        if i + 1 < len(op3) :
            arranged_problems = arranged_problems + '    '

    # Line 4
    if solved :
        arranged_problems = arranged_problems + '\n'
        for i in range(len(solutions)) :
            max_len = max([len(op1[i]), len(op2[i])]) + 2
            for j in range(max_len - len(str(solutions[i]))) :
                arranged_problems = arranged_problems + ' '
            arranged_problems = arranged_problems + str(solutions[i])
            if i + 1 < len(solutions) :
                arranged_problems = arranged_problems + '    '

    return arranged_problems