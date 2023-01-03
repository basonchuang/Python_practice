class date:
    def __init__(self, y, m, d):
        v_y = y
        v_m = m
        v_d = d

class days:
    def __init__(self, d):
        value = d
class weeks:
    def __init__(self, w):
        value = w
class months:
    def __init__(self, m):
        value = m
    def __add__(self, RHS):
        pass
    def __sub__(self, RHS):
        pass
    def __radd__(self, LHS):
        pass
    def __rsub__(self, LHS):
        pass

class today:
    def __init__(self):
        value = date(2023,1,3)
class tomorrow:
    def __init__(self):
        return date(2023,1,4)
class yesterday:
    def __init__(self):
        return date(2023,1,2)

def eval(list):
    stack = []
    for item in list:
        stack = operation(item, stack)
def operation(item, stack):
    if item is date:
        pass
        #stack.append(item)
    if item is days:
        pass
    if item is today:
        stack.append(today.value)
    if item is tomorrow:
        pass
    if item is yesterday:
        pass
    if item == 'add':
        pass
    if item == 'sub':
        pass
    if item == 'swap':
        pass
    print(stack)
    return stack
if __name__ == '__main__':
    eval([today])