f = open("input")
w1, w2 = f
w1 = w1.split(',')
w2 = w2.split(',')

p1 = []
p2 = []
for w in w1:
    d = w[0]
    l = int(w[1:])
    x, y = 0, 0
    if d == 'U': y += 1
    if d == 'D': y -= 1
    if d == 'L': x -= 1
    if d == 'R': x += 1
    p1.append((x, y))

for w in w2:
    d = w[0]
    l = int(w[1:])
    x, y = 0, 0
    if d == 'U': y += 1
    if d == 'D': y -= 1
    if d == 'L': x -= 1
    if d == 'R': x += 1
    p2.append((x, y))

print(set(p1).intersection(set(p2)))
