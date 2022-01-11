import re


def getAttributes(expr):
    expr = expr.split("(")[1:]
    expr = "(".join(expr)
    expr = expr[:-1]
    expr = re.split("(?<!\(.),(?!.\))", expr)
    return expr

def getInitialPredicate(expr):
    return expr.split("(")[0]

def isConstant(char):
    return char.isupper() and len(char) == 1

def isVariable(char):
    return char.islower() and len(char) == 1

def replaceAttributes(expr, old, new):
    attr = getAttributes(expr)
    for index, val in enumerate(attr):
        if val == old:
            attr[index] = new
    predicate = getInitialPredicate(expr)
    return predicate + "(" + ",".join(attr) + ")"

def apply(expr, subs):
    for sub in subs:
        new, old = sub  #substitution is a tuple of 2 values (new, old)
        expr = replaceAttributes(expr, old, new)
    return expr
def checkOccurs(var, expr):
    if expr.find(var) == -1:
        return False
    return True

def getFirstPart(expr):
    attr = getAttributes(expr)
    return attr[0]

def getRemainingPart(expr):
    predicate = getInitialPredicate(expr)
    attr = getAttributes(expr)
    newExpr = predicate + "(" + ",".join(attr[1:]) + ")"
    return newExpr

def unify(exp1, exp2):
    if exp1 == exp2:
        return []

    if isConstant(exp1) and isConstant(exp2):
        if exp1 != exp2:
            return False

    if isConstant(exp1):
        return [(exp1, exp2)]

    if isConstant(exp2):
        return [(exp2, exp1)]

    if isVariable(exp1):
        if checkOccurs(exp1, exp2):
            return False
        else:
            return [(exp2, exp1)]

    if isVariable(exp2):
        if checkOccurs(exp2, exp1):
            return False
        else:
            return [(exp1, exp2)]

    if getInitialPredicate(exp1) != getInitialPredicate(exp2):
        print("Predicates do not match. Cannot be unified")
        return False

    attributeCount1 = len(getAttributes(exp1))
    attributeCount2 = len(getAttributes(exp2))
    if attributeCount1 != attributeCount2:
        return False

    head1 = getFirstPart(exp1)
    head2 = getFirstPart(exp2)
    initialSub = unify(head1, head2)
    if not initialSub:
        return False
    if attributeCount1 == 1:
        return initialSub

    tail1 = getRemainingPart(exp1)
    tail2 = getRemainingPart(exp2)

    if initialSub != []:
        tail1 = apply(tail1, initialSub)
        tail2 = apply(tail2, initialSub)

    remainingSub = unify(tail1, tail2)
    if not remainingSub:
        return False

    initialSub.extend(remainingSub)
    return initialSub

exp1 = input("Expression1: ")
exp2 = input("Expression2: ")
subs = unify(exp1, exp2)
print("Substitutions: ")
print(subs)
