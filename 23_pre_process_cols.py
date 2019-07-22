# Consider	the	following	lines	of	text: 
# 30kg,inr2000,31.11,56.33,1 
# 52kg,inr8000.35,12,16.7,2 

#Let’s	try	to	ingest	this	
# data	in	a	NumPy	array	as	
# follows: 
import	numpy	as	np
from io import StringIO
in_data	=	StringIO("30kg,inr2000,31.11,56.33,1\n52kg,inr8000.35,12,16.7,2") 
data	=	np.genfromtxt(in_data,delimiter=",") 
print(np.array(data))

