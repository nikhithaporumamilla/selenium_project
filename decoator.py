# def outer_div(func):
#     def inner(x,y):
#         if (x<y):
#             x,y = y,x
#         return func(x,y)
#     return inner
# @outer_div
#     print(x/y)
# divide(20,10)


# if i want to print 10 times
# def outer_div(func):
#     def inner():
#         for i in range(10):
#             func()
#     return inner
#
# @outer_div
# def foo():
#     print("HI")
#
# @outer_div
# def bar():
#     print("Hello")
#
# @outer_div
# def xxx():
#     print("Hello World")
#
# foo()
# bar()
# xxx()

#
# def dec(num):
#     def outer_div(func):
#         def inner(x):
#             for i in range(num):
#                 func(x)
#         return inner
#     return outer_div
#
# @dec(5)
# def foo(a):
#     print(a)
#
# @dec(10)
# def bar(b):
#     print(b)
#
# @dec(15)
# def xxx(c):
#     print(c)
#
# foo("Hi")
# bar("Hello")
# xxx("Hello World")

# def outer_div(func):
#     def inner(x,y):
#         if y==0:
#             return "zero division error"
#         return func(x,y)
#     return inner
# @outer_div
# def divide(x,y):
#     return x/y
# print(divide(10/0))
#
# def dec(func):
#     def inner(n):
#          a,b=0,1
#          result =[a]
#          while b<n:
#              result.append(b)
#              a, b = b, a + b
#          return func(n)
#     return inner
# @dec()
# def fib1(a,b):
#     return(a,b)
# fib1(100)


# def div(func):
#     def outer(x,y):
#         if y==0:
#             print("not true")
#             return func(x,y)
#         return outer
# @div
# def divide(x,y):
#     return(x/y)
# print(divide(10/0))



def outer(func):
    def inner(a):
        func(a)
    return inner
@outer
def bar(text):
    print(text)
bar("hi")








