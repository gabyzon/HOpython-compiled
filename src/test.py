import ctypes as C
math = C.CDLL('./libmymath.a')

print( "4+3 = %d", math.add_int(3, 4) )
print( "7x3 = %d", math.dot_product(7, 3) )
print( "5.0 + 1.0 + %d", math.add_float(5.0, 1.0) )
