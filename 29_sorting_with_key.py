# The	attrgetter	and	methodcaller	comes	
# in	handy	when	the	elements	of	our	iterable	
# are class	objects.	Look	at	the	following	example: 
#	Let	us	now	enclose	the	employee	records	as	class	objects, 
from	operator	import	attrgetter 
class	employee(object):				
    def	__init__(self,name,id,age):								
        self.name	=	name								
        self.id	=	id								
        self.age	=	age				
    def	pretty_print(self):							
        print(self.name, self.id, self.age)
#	Now	let	us	populate	a	list	with	these	class	objects.  
employee_records	=	[] 
emp1	=	employee('joe',1,53) 
emp2	=	employee('beck',2,26) 
emp3	=	employee('ele',6,32)
employee_records.append(emp1) 
employee_records.append(emp2) 
employee_records.append(emp3)
# As	you	can	see,	the	order	of
# 	the	insertion	has	been	preserved.	
# Now,	let’s	use	attrgetter to	sort	
# the	list	with	the	age	field:
#	Print	the	records 
employee_records_sorted	=	sorted(employee_records,key=attrgetter('age'))
for	emp	in	employee_records_sorted:				
    emp.pretty_print()
