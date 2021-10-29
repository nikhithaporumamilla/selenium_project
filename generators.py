# print gen(20),gen (20,30),gen(20,30,2) in one function we have to write

def gen(num,num1=0,z=1):
    # print(num,num1,z)
    if num>num1:
        num,num1=num1,num
    while num < num1:
        yield(num)
        num += z

a = gen(20)
print(a)
while True:
    print(next(a))


