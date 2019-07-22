a	=	[8,	0,	3,	4,	5,	2,	9,	6,	7,	1]
print	(a) #[8,	0,	3,	4,	5,	2,	9,	6,	7,	1]
a.sort(reverse=True)
print	(a) # [9,	8,	7,	6,	5,	4,	3,	2,	1,	0] 
#Now,	we	have	a	descending	order	sorting. 
# For	other	iterables,	we	have	to	fall	
# back	on	the	sorted	function.	
# Let's	look	at	a	tuple	example:
a	=	(8,	0,	3,	4,	5,	2,	9,	6,	7,	1)
sorted(a) # [0,	1,	2,	3,	4,	5,	6,	7,	8,	9]
print(sorted(a))
