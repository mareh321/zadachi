a = input()
b = eval(input())
c = dict(zip(b,a))
f = ''
for i in range(len(a)):
 f += c.setdefault(i)
print(f)