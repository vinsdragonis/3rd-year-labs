# Knowledge-Base Entailment

## Objective

Given a knowledge-base using **propositional logic**, prove the given query using **resolution**.

## Notation

    variables = [p, q, r]
    symbols/operators = [
        NOT: ~
        OR: v
        AND: ^
    ]

## Logic

In resolution, we are given a **knowledge base** and a **query**. We test to see if *the given knowledge base enatils the given query*.

    function entailment():
        for comb in combinations:
            s = evaluatePostfix(toPostfix(kb), comb)
            f = evaluatePostfix(toPostfix(q), comb)
            if s and not f:
                return False
        return True
        
            
## Utility Functions

1. `CheckEntailment()` - Checks if the given **knowledge base** entails the given **query**
2. `eval(i, a, b)` - Evaluates and returns **a ^ b** if the given operation is ***ANDing***, else returns **a v b**
3. `isOperand(c)` - Checks if the given character is an operand or not
4. `isLeftParanthesis(c)` - Checks if the given character is an **opening paranthesis**
5. `isRightParanthesis(c)` - Checks if the given character is an **closing paranthesis**
6. `isEmpty(stack)` - Checks if the stack is empty
7. `peek(stack)` - Returns the top element in the stack
8. `hasLessOrEqualPriority(c1, c2)` - Checks the operator and returns if the given operator is of lower, equal or higher priority
9. `toPostfix(infix)` - Converts the given knowledge base and query to **postfix**
10. `evaluatePostfix(exp, comb)` - Evaluates the given postfix expression
