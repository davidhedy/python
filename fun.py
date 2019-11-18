data = 5




def func(a,b):
    a = 15
    def fun2(a, b):
        # nonlocal a
        a += 5
    fun2(23,10)
    print(a)
    a = [1,2,3]
    print("id inner:",id(a))
    return a
