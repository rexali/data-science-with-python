#	Importing	numpy	as	np 
import	numpy	as	np

#	A	simple	function	to	examine	given	numpy	object	
def	display_shape(a):				
    print	("")				
    print	(a)				
    print	("")			
    print	( "Number	of	elements	in	a	=	%d" %(a.size) )				
    print	("Number	of	dimensions	in	a	=	%d" %(a.ndim) )				
    print	("Rows	and	Columns	in	a	", a.shape)				
    print	("")
# Armed	with	the	knowledge	of	array	and	matrix	
# creation,	let’s	see	some	shaping operations: 
# Recipe_1e.py 
#	Array	shaping 
a_matrix	=	np.arange(9).reshape(3,3) 
display_shape(a_matrix)
print("Array shaping")

#	Paramter	-1	refers	to	as	many	as	
# dimension	needed 
back_to_array	=	a_matrix.reshape(-1) 
display_shape(back_to_array)
print("Array shaping wth -1")

#Recipe_1f.py 
#	Matrix	operations 
e_matrix	=	np.arange(9).reshape(3,3) 
f_matrix	=	np.arange(9).reshape(3,3)
print	("f_matrix, row sum",f_matrix.sum(axis=1))
print("matrix sum along axix=1")

#Recipe_1g.py 
#	reversing	elements 
display_shape(f_matrix[::-1])
print("reversed element")

# reverse to list
e	=	e_matrix.flatten() 
print(e)
print("reverse to list")

# The	ravel	and	flatten	functions	can	be	used	
# to	convert	a	matrix	to	a	one-dimensional array: 
a_matrix	=	np.arange(9).reshape(3,3) 
back_array	=	np.ravel(a_matrix) 
display_shape(back_array)
print("reverse matrix to one dimensional array")

a_matrix	=	np.arange(9).reshape(3,3) 
back_array	=	a_matrix.flatten() 
display_shape(back_array)
print("reverse to list")


# Let’s	look	at	some	random	number	generation	
# routines	in	the	NumPy	library: #
# Recipe_1h.py 
#	Random	numbers 
general_random_numbers	=	np.random.randint(1,100,	size=10) 
print	(general_random_numbers)
print("general random number")

uniform_rnd_numbers	=	np.random.normal(loc=0.2,scale=0.2,size=(3,3))
print	(uniform_rnd_numbers)
print("uniform random number")


