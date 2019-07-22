# Let’s	pass	two	sequences	to	a	
# zip	function	and	print	the	output
zip_list = list(zip(range(1,5),range(1,5)))
print(zip_list)
# check this
#x,y	=	zip(*out) 
#print	(x,y) 
a	=(2,3) 
print	(pow(*a))
# The	power	operation	takes	two	arguments.	
# Now	a	is	a	tuple;	as	you	can	see,	
# the	*	operator splits	the	tuple	into	two	separate	arguments.	
# *	operator	unpacks	the	tuple	in	2	and	3. 
# They	are	passed	as	parameters,	pow(2,3),	and	we	get	the	output,	8. 
# The	**	operator	can	be	used	to	unpack	a	dictionary.	
# Look	at	the	following	snippet: 
a_dict	=	{"x":10,"y":10,"z":10,"x1":10,"y1":10,"z1":10}
def	dist(x,y,z,x1,y1,z1): 
    return	abs((x-x1)+(y-y1)+(z-z1))
print(dist(**a_dict)) # 0
# Armed	with	these	two	operators,	we	can	write	
# a	function	without	any	restrictions	
# on	the number	of	variables	that	it	can	ingest: 
def	any_sum(*args): 
    tot	=	0 
    for	arg	in	args: 
        tot+=arg 
    return	tot
print	(any_sum(1,2))  #3
print	(any_sum(1,2,3)) #6