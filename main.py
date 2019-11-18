# from fun import func 
import fun

if __name__ == '__main__':
	aa = 5
	bb = 3
	fun.data = 15
	f = fun.func(aa, bb)
	print("id of f is ",id(f))
	# print("sum is ",fun.func(aa, bb))
	# print(fun.data)