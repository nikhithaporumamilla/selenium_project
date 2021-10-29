def myfunc(a):
    return len(a)
x = map(myfunc,('apple','banana','mango'))
# print(x)
#
# print(list(x))

#
# a = (1,4,5,3,6,54,2)
# x=sorted(a,reverse=True)
# print(x)

#
# x=pow(1,2)+5,pow(2,2)+5
# print(x)

# write even number from 1 to 100 using list comprehension
# num=range(100)
# lst=[i for i in range(100) if i % 2 == 0]
# print(lst)
# for i in num:
#     if num % 2==0:
#         print("even numbers:")
#     else:
#         print("odd numbers:")


#
# def func(x):
#     return x["marks"]
# l.sort(key=func)
# l
# [{'name': 'munna', 'marks': 518}, {'name': 'xyz', 'marks': 530}, {'name': 'nikki', 'marks': 550}]

#dict comprehension:
# =[1, 2, 3, 4, 5]
# # d = {i: i * i for i in l}
# # print(d)
# l=[1,2,3,4,5]
# # l={1:1,2:4,3:9,4:16,5:25}
# d={i:i*i for i in l if i%2==0}
# print(d)

#
# f = lambda x:pow(x,5)+5
# print (f(5))
#
# try:
#     print("hello")
# except:
#     print("something went wrong")
# else:
#     print("nothing went wrong")


# list1=[1,2,3,4,5]
# lst=[]
# for i in list1:
#     if i%2 ==0:
#         lst.append(i+2)
#     else:
#         lst.append(i+1)
# print(lst)


# 0,1,1,2,3,5,8,13
#
# def fib(a,b):
#     while b<100:
#         yield(a)
#         a,b=b,a+b
# niki=fib(0,1)
# while True:
#     print(next(niki))
#



#
# lst=[i+2 if i%2==0 else i+1 for  i in list1]
# print(lst)
