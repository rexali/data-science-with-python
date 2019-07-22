# Let’s	start	by	creating	
# some	simple	matrices	
# and	arrays: 
# Recipe_1a.py 
#	Importing	numpy	as	np 
import	numpy	as	np 
#	Creating	arrays 
a_list	=	[1,2,3] 
an_array	=	np.array(a_list) 
#	Specify	the	datatype 
an_array	=	np.array(a_list,dtype=float)
print(an_array)
print	("")

#	Creating	matrices 
a_listoflist	=	[[1,2,3],[5,6,7],[8,9,10]] 
a_matrix	=	np.matrix(a_listoflist,dtype=float)
print(a_matrix)

# Now	we	will	write	a	small	
# convenience	function	in	order	
# to	inspect	our	NumPy	objects: 
# Recipe_1b.py 
#	A	simple	function	to	examine	given	numpy	object	
def	display_shape(a):				
    print	("")				
    print	(a)				
    print	("")			
    print	( "Number	of	elements	in	a	=	%d" %(a.size) )				
    print	("Number	of	dimensions	in	a	=	%d" %(a.ndim) )				
    print	("Rows	and	Columns	in	a	", a.shape)				
    print	("")
display_shape(a_matrix)

#Let’s	see	some	alternate	ways	of	creating	arrays: 
# Recipe_1c.py 
# Alternate	ways	of	creating	arrays 
#   1.	Leverage	np.arange	to	create	numpy	array 
created_array	=	np.arange(1,10,dtype=float) 
display_shape(created_array)
#	2.	Using	np.linspace	to	create	numpy	array 
created_array	=	np.linspace(1,10) 
display_shape(created_array)
#	3.	Create	numpy	arrays	in	using np.logspace 
created_array	=	np.logspace(1,10,base=10.0) 
display_shape(created_array)
#	Specify	step	size	in	arange	while	creating 
#	an	array.	This	is	where	it	is	different 
#	from	np.linspace 
created_array	=	np.arange(1,10,2,dtype=int) 
display_shape(created_array)
