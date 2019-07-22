# The	methodcaller	can	be	used	
# to	sort	when	we	want	to
# 	use	a	method	in	our	class	to decide	
# the	sorting.	For	demonstration	purposes,	
# let’s	add	a	random	method,	which	
# divides the	age	by	the	ID: 
class employee(object):
    def	__init__(self,name,id,age):		
        self.name	=	name								
        self.id	=	id								
        self.age	=	age

    def	pretty_print(self):
        print(self.name,self.id,self.age)

    def	random_method(self):							
        return	self.age/self.id

#	Populate	data 
employee_records	=	[] 
emp1	=	employee('joe',1,53) 
emp2	=	employee('beck',2,26) 
emp3	=	employee('ele',6,32)

employee_records.append(emp1) 
employee_records.append(emp2) 
employee_records.append(emp3)

from	operator	import	methodcaller 
# We	can	now	sort	the	list	by	calling	this	method:methodcaller
employee_records_sorted	=sorted(employee_records,key=methodcaller('random_method')) 
for	emp	in	employee_records_sorted:				
    emp.pretty_print()	
 
