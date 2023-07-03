x = ('1','2','3','4','5','6')
print(type(x))

y = ('a',)
print(type(y))

y = ('a')
print(type(y))

t1 = tuple('matrix')
print(t1)
print(t1[2])
print(t1[1:3])

t1 = ('1',) + t1[1:]
print(t1)

x = ('1','2','3') < ('0','1','2')
print(x)

