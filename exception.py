# try:
#     d = {"siva":518,"reddy":530}
#     l=[10,20,30]
#     name=input("please enter the name:")
#     print(d[name])
# except:
#     print("Got exception")
# else:
#     print("no exception")
# finally:
#     print("finally block")



# try:
#      d={"siva":518,"reddy":540}
#      l = [10,20,30]
#      name = input("please enter the name:")
#      print(d[name])
# except Exception as e:
#      print("Got exception",e)


# try:
#     d = {"siva": 518, "reddy": 540}
#     l = [10,20,30]
#     name = input("please enter the name:")
#     print(d[name])
#     index=int(input("please enter the index:"))
#     print(l[index])
# except KeyError as ke:
#     print("Please enter a valid name:")
# except IndexError as ie:
#     print("please enter a valid index:")
# except Exception as e:
#     print("Got exception",e)


try:
    d = {"siva": 518, "reddy": 450}
    l = [10, 20, 30]
    name = input("Please enter the name: ")
    print(d[name])
    index = int(input("Please enter the index: "))
    print(l[index])
    # raise KeyError("Please enter a valid text....")
except KeyError as ke:
    print("Please enter a valid name.")
    print(ke)
except IndexError as ie:
    print("Please enter a valid index.")
except Exception as e:
    print("Got Exception", e)
