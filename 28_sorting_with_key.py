# Due	to	the	importance	of	sorting	by	a	key,	
# Python	provides	a	convenient	function	
# to access	keys	instead	of	writing	lambdas.	
# The	operator	module	has	the	itemgetter, attrgetter,	
# and	methodcaller	functions.	The	sorting	example	that	
# we	saw	can	be	written as	follows	using	itemgetter: 
from	operator	import	itemgetter 
employee_records	=[
    ('joe',1,53),('beck',2,26),
    ('ele',6,32),('neo',3,45),																				
    ('christ',5,33),('trinity',4,29),																					
    ] 
print	(sorted(employee_records,key=itemgetter(0))) 
""" [('beck',	2,	26),	('christ',	5,	33),	
     ('ele',	6,	32),	('joe',	1,	53),	
     ('neo',	3,	45),	('trinity',	4,	29)] 
""" 
print	(sorted(employee_records,key=itemgetter(1))) 
""" [('joe',	1,	53),	('beck',	2,	26),	
('neo',	3,	45),	('trinity',	4,	29),	
('christ',	5,	33),	('ele',	6,	32)] 
""" 
print	(sorted(employee_records,key=itemgetter(2))) 
""" [('beck',	2,	26),	('trinity',	4,	29),	
('ele',	6,	32),	('christ',	5,	33),	
('neo',	3,	45),	('joe',	1,	53)] 
""" 
# let’s	say	that	we	need	to	sort	
# by	name and	then	by	age,	
# our	code	would	be	as	follows:
print(sorted(employee_records,key=itemgetter(0,1)))
'''
[('beck',	2,	26),	
('christ',	5,	33),	
('ele',	6,	32),	
('joe',	1,	53),	
('neo',	3,	45),	
('trinity',	4,	29)]
'''