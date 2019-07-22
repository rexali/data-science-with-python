# 	In	this	case,	we	have	a	generator comprehension.	
# If	you	recall,	we	tried	doing	a	tuple	
# comprehension	in	this	way	and	got	a generator	object:
SimpleCounter		=	(x**2	for	x	in	range(1,10))
tot	=	0 
for	val	in	SimpleCounter:				
    tot += val
print(tot)

# Let’s	look	at	how	to	use	the	yield	statement	
# to	create	a	generator: 
def	my_gen(low,high):				
    for	x	in	range(low,high):								
        yield	x**2

tot	=	0								
for	val	in	my_gen(1,10):				
    tot+=val 
print (tot)

# In	the	previous	section,	
# we	mentioned	that	both	a	
# generator	and	iterables	produce	an iterator.	
# Let’s	validate	this	by	trying	to	call	
# the	generator	using	the	iter	function: 
gen	=	(x**2	for	x	in	range(1,10))
for	val	in gen:	# iter(gen): will also work				
    print(val) 

