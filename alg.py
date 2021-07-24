d = int(input('enter the dividend here:-'))
s = int(input('enter the divisor here:-'))
q = d // s
r = d % s
box = [[d, s, q, r]]

while r != 0:
    d = s
    s = r
    q = d // s
    r = d % s
    box.append([d, s, q, r])

print('dividend = divisor * quotient + reminder')
for _ in range(len(box)):
    print(box[_][0], ' = ', box[_][1], ' * ', box[_][2], ' + ', box[_][3])

if len(box) == 1:
    print('\nGCD is:- ', box[0][2])
elif len(box) > 1:
    print('\nGCD is:- ', box[-2][3])

length = len(box) - 2
ans = [box[length][0], 1, box[length][1], box[length][2]]
m, n = 0, 0

print(box[-2][0], ' - ', '(', box[-2][1], ')', box[-2][2], '\n')


def extend(size, ind):
    del (ans[ind])
    ans.insert(ind, box[size][0])
    ans.insert(ind + 1, box[size][1])
    ans.insert(ind + 2, box[size][2])
    if ind == 0:
        print('(', ans[0], ' - ', ans[1], '*', ans[2], ')', ans[3], ' - ', '(', ans[4], ')', ans[5])
    else:
        print(ans[0], '(', ans[1], ')', ' - ', '(', ans[2], '-', ans[3], '*', ans[4], ')', ans[5])
    return ans


def simplify(pos):
    global length
    if pos == 1:
        a = ans[1] + ans[4] * ans[-1]
        del (ans[1])
        del (ans[2])
        del (ans[2])
        ans.insert(1, a)
        length -= 1
    elif pos == 0:
        a = ans[2] * ans[3] + ans[-1]
        del (ans[1])
        del (ans[1])
        del (ans[-1])
        ans.append(a)
        length -= 1
    print(ans[0], '(', ans[1], ')', ' - ', ans[2], '(', ans[3], ')', '\n')


def evaluate():
    print('A * m  +   B * n   =   GCD')
    if (ans[0] * (-ans[1])) + (ans[2] * ans[3]) == box[-2][3]:
        print(ans[0], '* (', -ans[1], ') + ', ans[2], ' * (', ans[3], ') = ', box[-2][3])
        return
    elif (ans[0] * ans[1]) + (ans[2] * (-ans[3])) == box[-2][3]:
        print(ans[0], '* (', ans[1], ') + ', ans[2], ' * (', -ans[3], ') = ', box[-2][3])
        return
    elif (ans[0] * (-ans[1])) + (ans[2] * (-ans[3])) == box[-2][3]:
        print(ans[0], '* (', -ans[1], ') + ', ans[2], ' * (', -ans[3], ') = ', box[-2][3])
        return
    elif (ans[0] * (ans[1])) + (ans[2] * (ans[3])) == box[-2][3]:
        print(ans[0], '* (', ans[1], ') + ', ans[2], ' * (', ans[3], ') = ', box[-2][3])
        return
    else:
        pass


right = True
left = False
if length >= 0:
    while length != 0:
        if right:
            extend(length - 1, 2)
            simplify(1)
            right = False
            left = True
        elif left:
            extend(length - 1, 0)
            simplify(0)
            right = True
            left = False
    evaluate()
else:
    print('cannot find the M and N')
