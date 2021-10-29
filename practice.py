# l=[1,2,3,4,5]
# # d = {}
# # for i in l:
# #     d[i]=i*i
# #     print(d)
#
# # list cmprsn:
# d={i:i*i for i in l if i%2==0}
# print(d)

# def dec(func):
#     def inner():
#         x=func()
#         return f"Hi {x} How ru "
#     return inner
#
# @dec
# def foo():
#     return "munna"
# @dec
# def bar():
#     return "niki"
#
# print(foo())
# print(bar())

# def dec(func):
#     def inner(x,y):
#         if  x>10:
#             x=x-5
#         else:
#             x=x+5
#         y=y-5 if y>10 else y+5
#         func(x,y)
#     return inner
# @dec
# def foo(a,b):
#     print(a,b)
# @dec
# def bar(c,d):
#     print(c,d)
#
# foo(2,12)
# bar(3,15)
#
# a = lambda x,y:x+y
# a

# f= filter(lambda x:x%2==0,range(100))
# print(list(f))

# if you want to perform same functionality on each and every element of the sequence.. then we need to use map

a=[2,  12, 6, 16, 5, 7]
# z=list(map(lambda x:x-5 if x>=10 else x+5,a))
# print(z)

lst=[i-5 if i>=10 else i+5 for i in a]
print(lst)


