# Let’s	import	the	necessary	libraries	to	start	with.	
# We	will	proceed	to	define	a	sample	input. 
# Finally,	we	will	demonstrate	how	to	process	tabular	data.

#	1.	Let	us	simulate	a	small	tablular	

# input	using	StringIO 
import	numpy	as	np
from io import StringIO 
in_data	=	StringIO("10,20,30\n56,89,90\n33,46,89")
#	2.Read	the	input	using	numpyâ€™s	
# genfromtext	to	create	a	nummpy	array. 
data	=	np.genfromtxt(in_data,dtype=int,delimiter=",")
print(np.array(data))
#	cases	where	we	may	not	need	
# to use	some	columns. 
in_data	=	StringIO("10,20,30\n56,89,90\n33,46,89") 
data	=	np.genfromtxt(in_data,dtype=int,delimiter=",",usecols=(0,1))
print(np.array(data))
#	providing	column	names 
in_data	=	StringIO("10,20,30\n56,89,90\n33,46,89") 
data	=	np.genfromtxt(in_data,dtype=int,delimiter=",",names="a,b,c")
print(np.array(data))
#	using	column	names	from	data 
in_data	=	StringIO("a,b,c\n10,20,30\n56,89,90\n33,46,89") 
data	=	np.genfromtxt(in_data,dtype=int,delimiter=",",names=True)
print(np.array(data))




 