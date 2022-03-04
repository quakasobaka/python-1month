def get_sign(i):
    if i[0] in '+-':
        return i[0]
# Дан список:
list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
s = 0
while s < len(list):
    sign = get_sign(list[s])
    if list[s].isdigit() or (sign and list[s][1:].isdigit()):
        if sign:
            list[s] = sign + list[s][1:].zfill(2)
        else:
            list[s] = list[s].zfill(2)
        list.insert(s, '')
        list.insert(s + 2, '')
        s += 2
    s += 1
print(list)
list2 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list1 = len(list2)
for _ in range(list1):
    s = list2.pop(0)
    if s.isdigit():
        list2.append(f'"{int(s):02d}"')
    elif s[0] == "+" and s[1].isdigit():
        list2.append(f'"+{int(s):02d}"')
    else:
        list2.append(s)
print(' '.join(list2))