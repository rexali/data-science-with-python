#First	let	us	declare	a	list.
a	= [10,20,30] 
#	Let	us	now	call	the	map	function in	our	Print
# 	statement.
b = map(lambda x:x**2, a) 
print (list(b))

# Similarly,	any	other	function	can	be	
# applied	to	a	list: 
print	(list(map(lambda	x:x**3,a)))
# Using	map,	we	can	replace	the	code	
# snippet	in	the	previous	recipe	with	
# a	single	line: 
print	(sum(map(lambda	x:x**2,a)) )
print	(sum(map(lambda	x:x**3,a)) )

a	=[10,20,30] 
b	=	[1,2,3]
print	(list(map(pow,a,b)))