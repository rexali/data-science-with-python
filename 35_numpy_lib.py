import	numpy	as	np
# Let’s	look	at	some	matrix	operations,
a_matrix	=	np.arange(9).reshape(3,3)
b_matrix	=	np.arange(9).reshape(3,3)	
# such	as	addition: 
c_matrix	=	a_matrix	+	b_matrix 
#We	will	also	look	at	element-wise	multiplication:
d_matrix	=	a_matrix	*	b_matrix 
print(d_matrix)
print("")
#The	following	code	shows	a	matrix	
# multiplication	operation:
e_matrix	=	np.dot(a_matrix,b_matrix)
print(e_matrix) 
print("")
# Finally,	we	will	transpose	a	matrix: 
f_matrix	=	e_matrix.T 

print(f_matrix)
# The	min	and	max	functions	can	be	used	
# to	find	the	minimum	and	maximum	elements	in	
# a matrix.
	
# The	sum	function	can	be	used	to	find	t
# he	sum	of	the	rows	or	columns	in	a	matrix: 
print ("")
print(	"f_matrix,minimum	=	%d"%(f_matrix.min()) )
print(	"f_matrix,maximum	=	%d"%(f_matrix.max()) )
print(	"f_matrix,	col	sum",f_matrix.sum(axis=0) )
print	("f_matrix,	row	sum",f_matrix.sum(axis=1))


# The	copy	function	can	be	used	to	
# copy	a	matrix,	as	follows: #	Like	
# python	all	elements	are	used	by	reference 
# if	copy	is	needed	copy()	command	is	used 
f_copy	= f_matrix.copy()
print("") 
print(f_copy)
print("copied matrix")

# Finally,	let’s	look	at	the	mgrid	functionality: 
# Grid	commands 
#Let’s	see	the	first	element	of	each	array.	[0,0,0]	is	the	first	
# coordinate	in	our	threedimensional	space.	
# The	second	element	in	all	three	arrays,	[0,0,1]	is	
# another	point	in	our space.	Similarly,	using	mgrid,	
# we	captured	
# all	the	points	in	our	three-dimensional coordinate	system. 
xx,yy,zz	=	np.mgrid[0:3,0:3,0:3] 
xx	=	xx.flatten() 
yy	=	yy.flatten() 
zz	=	zz.flatten()
print(xx)
print(yy)
print(zz)
print('In	each	dimension,	our	values	range	from	0 to	3.')

