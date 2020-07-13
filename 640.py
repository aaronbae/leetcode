class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        # add all coefficients of x
        # add all constnats
        import re
       
        first, second = equation.split("=")
        def calculate(expression):
            coefficients = 0
            constants = 0
            terms = " ".join(re.split(r"[^a-zA-Z0-9]",expression)).split()
            operators = " ".join(re.split(r"[a-zA-Z0-9]",expression)).split()
            if len(operators) < len(terms):
                operators = ["+"] + operators
            for i in range(len(terms)):
                t = terms[i]
                op = 1 if operators[i]=="+" else -1 
                if t.endswith("x"):
                    coefficients += op * int(t[:-1]) if len(t) > 1 else op
                else:
                    constants += op * int(t)
            return coefficients, constants

        a,b = calculate(first)
        c,d = calculate(second)
        final_coefficient_left = a - c
        final_constant_right = d - b
        if final_coefficient_left == 0:
            if final_constant_right == 0:
                return "Infinite solutions"
            else: 
                return "No solution"
        else:
            return "x="+str(int(final_constant_right/final_coefficient_left))
        
a =  Solution()
equation= "-x=-1"
print(a.solveEquation(equation))