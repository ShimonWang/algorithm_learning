#https://blog.csdn.net/weixin_45111135/article/details/135595380 参考教程

a = input()

#%%
a = input().split()
b = input().split(',')
print(a)
print(b)

#%%
a = int(input())

b = input().split()
c = [int(i) for i in b]

d = [int(i) for i in input().split()]

#%%
e = map(int, input().split())
f = list(e)
g = list(map(int, input().split()))

#%%
while True:
    try:
        data = input()
        # solve(data)
        pass
    except:
        break

#%%
n = int(input())
for _ in range(n):
    data = input()
    # solve(data)
    pass

#%%
while True:
    data = input()
    if judge(data):
        break
    solve(data)

#%%
# import sys

# print(*object, sep='', end='\n', file=sys.stdout, flush=False)

a = 1
b = 2
c = 3
print(a)

print(a, b, c)

print(a, b, c, sep=',')

res = [1,2,3]
print(res)
for i in range(len(res)):
    print(res[i])

for i in range(len(res)):
    print(res[i], end=' ')

#%%
res = ['a', 'b', 'c']
print("".join(res))

print("*".join(res))