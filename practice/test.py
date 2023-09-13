arr = [1, 2, 1, 2, 1, 3]
k = 4

obj = {}

for x in arr:
    if x in obj:
        obj[x] += 1
    else:
        obj[x] = 1
n = len(arr)

res = []



for x in range(n, 0, -1):
    for ob in obj:

        if obj[ob] == x:
            print(x)
            res.append(ob)


print(res[:k])