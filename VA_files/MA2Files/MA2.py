"""
Solutions to module 2 - A calculator
Student: Ellen Lodin
Mail: ellen.lodin@telia.com
Reviewed by: Anton O'nils
Reviewed date: 2024-09-20
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper

#Errors

class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

#Functions l

def sin(x): 
    return math.sin(x)

def cos(x):
    return math.cos(x)

def exp(x):
    return math.exp(x)

def tan(x):
    return math.tan(x)

def fac(x):
    if (x//1) != x or x<0: 
       raise EvaluationError(f'Argument to fac is {x}, must be integer > 0')
    else: 
        return math.factorial(int(x))

def log(x):
    if x<= 0:
        raise EvaluationError(f'Argument to log is {x}, must be > 0')
    else: 
        return math.log(x)
    
def fib(x):
    memory = {}
    def _fib(x):
        if x < 0:
            raise EvaluationError(f'Argument to fib is {x}. Must be integer >= 0')
        elif x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            key1 = x - 1
            key2 = x - 2

            if key1 in memory:
                k1 = memory[key1]
            else: 
                k1 = _fib(key1)
                memory[key1] = k1

            if key2 in memory: 
                k2 = memory[key2]
            else:
                k2 = _fib(key2)
                memory[key2] = k2

            return k1 + k2
        
    return _fib(x)
   
#Functions n

def arglist(wtok, variables):
    arg = [] 
    if wtok.get_current() == '(':
        wtok.next()
        if wtok.get_current()!= ')':
            arg.append(expression(wtok, variables))
            while wtok.get_current()== ',':
                wtok.next()
                arg.append(expression(wtok, variables))
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ',' or ')' before arguments")
        wtok.next()  
    else: 
        raise SyntaxError("Expected '(' before arguments")
    return arg

def mean(x):
    return sum(x)/len(x)

def std(x):
    if not x: 
        raise EvaluationError('Missing data')
    else:
        mean_x = mean(x)
        variance_sum = 0
        for i in x: 
            variance_sum += (i-mean_x) ** 2
        variance = variance_sum / len(x)
        std = variance ** 0.5
        return std

#Global dictionaries 

function_l = {'sin':sin, 'cos':cos, 'log':log, 'exp':exp, 'fac': fac, 'tan': tan, 'fib':fib}
function_n = {'max': max, 'sum': sum, 'min':min, 'mean': mean, 'std':std}
immutible_variables = ['PI', 'E']

#Functions

def statement(wtok, variables):
    """ See syntax chart for statement"""
    #EOL = End Of Line
    result = assignment(wtok, variables)
    if wtok.has_next():
        raise SyntaxError(f"Unexpected token: {wtok.get_current()}")
    return result

def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    results = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            var_name = wtok.get_current()
            if var_name in immutible_variables:
                raise SyntaxError(f'Can not change a non-adjustable constant') #Are you able to change the value of PI? If yes, how can you fix this?
            else:
                variables[var_name] = results
            wtok.next()
        else:
            raise SyntaxError('Expected a variable after "="')
    return results

def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        if wtok.get_current() == '+': 
            wtok.next()
            result = result + term(wtok, variables)
        elif wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)
    return result

def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/':
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        elif wtok.get_current() == '/':
            wtok.next()
            divisor = factor(wtok, variables) 
            if divisor != 0:
                result = result / divisor
            else:
                raise EvaluationError("Division by zero")
    return result

def factor(wtok, variables):
    """ See syntax chart for factor"""
    if wtok.get_current() == '-':
        wtok.next()
        result = - factor(wtok, variables)

    elif wtok.get_current() == '+':
        wtok.next()
        result = factor(wtok, variables)

    elif wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise TokenError()
        wtok.next()

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() in variables:
        var_name = wtok.get_current()
        result = variables[var_name]
        wtok.next()
    
    elif wtok.get_current() in function_l: 
        func_name = wtok.get_current()
        wtok.next()
        if wtok.get_current() != '(':
            raise SyntaxError("Expected '('")
        wtok.next()
        arg = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise TokenError()
        result = function_l[func_name](arg)
        wtok.next()
    
    elif wtok.get_current() in function_n: 
        func = wtok.get_current()
        wtok.next()
        args = arglist(wtok, variables)
        result = function_n[func](args)

    elif  wtok.is_name():
        raise EvaluationError(f'Undefined variable: {wtok.get_current()}')

    else:
        raise SyntaxError(
            "Expected number or '('")  
    return result

def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        
        elif wtok.get_current() == 'vars':
            for key, value in variables.items():
                print(f"{key:4} : {value}")
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except EvaluationError as ee:
                print("*** Evaluation error: ", ee)
                print(f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
                print(f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

if __name__ == "__main__":
    main()
