from pythonds.basic.stack import Stack


def sol(st):
    s = Stack()
    sols = '"'
    for i in range(1, len(st) - 1):
        if st[i] == '(':
            s.push(st[i])
            if s.size() != 1:
                sols += st[i]
        else:
            s.pop()
            if not s.isEmpty():
                sols += ')'
    return sols + '"'


string = '"()()"'
print(sol(string))
