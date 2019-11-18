aa = 5

import ctypes

t = [1,2,3]
tid = id(t)
print(tid)
# t = "hello"
# print(id(t2))
t1 = ctypes.cast(tid, ctypes.py_object).value


print("t1：",t1,",", id(t1))


class test(object):
	def __init__(self, name):
		self.name = name
		print("create memory for object:", self.name)

	def __del__(self):
		print("release memory of ",self.name)


def fun():
    a = 15
    def fun2():
      nonlocal a
      b = a + 5
      a = 10
      print("a in fun2：",a)
    fun2()
    return a

a_out = fun()
print(a_out)

a_out = test("python");
print("a_out", type(a_out))

a_out = test("cpp")
print("hell world")



