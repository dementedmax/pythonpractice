openSymbols = {"(":1, "[":2, "{":3}
closeSymbols = {")":1, "]":2, "}":3}

def Check(string):
    string = list(string)
    stack = []

    for s in string:
        if s in openSymbols:
            stack.append(openSymbols.get(s))
        else:
            if bool(stack):
                if(stack[-1] == closeSymbols.get(s)):
                    stack.pop()
                else:
                    return False
            else:
                return False
    
    return not bool(stack)

print(Check("(())"))
print(Check("(()"))
print(Check("())"))
print(Check("))"))

print(Check("[[]]"))
print(Check("[[]"))
print(Check("[]]"))
print(Check("]]"))

print(Check("{{}}"))
print(Check("{{}"))
print(Check("{}}"))
print(Check("}}"))