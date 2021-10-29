# class Car:
#     has_sterio = True
#
#     def engine(self, a):
#         print(f"Engine {a}")
#
#     def wheels(self, val):
#         print(f"wheels {val}")
#
# driver = Car()
# driver.wheels("MRF")
# driver.engine("1500 CC")
# print(f'Has Sterio  {driver.has_sterio}')


class Car:
    has_sterio = True
    def __init__(self, car_type):
        # This loads along with the class
        # takes parameters that we pass
        # while creating object
        print(car_type)

    def engine(self, a):
        print(f"Engine {a}")

    def wheels(self, val):
        print(f"wheels {val}")

driver = Car("BMW")
driver.wheels("MRF")



# class Car:
#     has_sterio = True
#     def __init__(self, car_type):
#         # converting function level variable to class level variable
#         self.car_type = car_type
#         print(car_type)
#
#     def engine(self, a):
#         print(f"Engine {self.car_type} - {a}")
#
#     def wheels(self, engine_type, val):
#         self.engine(engine_type)
#         print(f"wheels {val}")
#
# driver = Car("BMW")

#
# class Car:
#     # __is_sterio = False
#
#     def engine(self):
#         print ("Engine")
#
#     def __body(self):
#         print("Body")
#
# obj = Car()
# obj.engine()
# obj._Car__body()

#
# # Multi level inheritance
# class Car:
#
#     def engine(self, a):
#         print(f"Engine {a}")
#
#
# class BMW(Car):
#
#     def wheels(self, xyz):
#         print(f"BMW Wheels - {xyz}")
#
#
# class BmwAG(BMW):
#
#     def body(self, abc):
#         self.wheels("MRF")
#         self.engine("1500 CC")
#         print(f"Body -{abc}")
#
# bmw = BmwAG()
# bmw.body("Metal")


# Multiple inheritance
# class Car:
#     def engine(self, a):
#         print(f"Car Engine {a}")
#
# class Maruthi(Car):
#     def engine(self, a):
#         print(f"Maruthi Engine {a}")
#
#
# class Suzuki(Car):
#
#     def engine(self, a):
#         print(f"Suzuki Engine {a}")
#
#
# class Maruthi800(Maruthi, Suzuki):
#
#     def engine(self, a):
#         print(f"Maruthi800 Engine {a}")
#
#     def body(self, abc):
#         self.engine("1500 CC")
#
# obj = Maruthi800()
# obj.body("Metal") #Maruthi800 --> Maruthi --> Suzuki --> Car


# class Car:
#
#     def engine(self, a):
#         print(f"Engine {a}")
#
#     def wheels(self, val):
#         print(f"wheels {val}")
#
#
# class BMW(Car):
#
#     def wheels(self, xyz):
#         print(f"BMW Wheels - {xyz}")
#
#     def body(self):
#         # print("Metal Body")
#         self.engine("1500 cc")
#         self.wheels("MRF")
#         super(BMW, self).wheels("MRF")# to access super class properties
#
# bm = BMW()
# bm.body()