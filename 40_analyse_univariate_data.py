# source of data save as .txt:
# For	this	example,	
# we	will	use	a	number	of	Presidential	Requests	of	Congress	in	State	of the	Union	Address.	The	following	URL	contains	
# the	data: http://www.presidency.ucsb.edu/data/sourequests.php 

#	Load	libraries 
import	numpy	as	np 
from	matplotlib.pylab import	frange 
import	matplotlib.pyplot	as	plt

# load data and preprocess it
# Load	the	data	and	handle	missing	values
fill_data	=	lambda	x	:	int(x.strip()	or	0)
data = np.genfromtxt('president.txt',dtype=(int,int),converters= {1:fill_data},	delimiter=",") 
x	=	data[:,0] 
y	=	data[:,1]

# 2.Plot	the	data	to	look	
# for	any	trends	or	values 
plt.close('all') 
plt.figure(1) 
plt.title("All	data") 
plt.plot(x,y,'ro') 
plt.xlabel('year')
plt.ylabel('No	Presedential	Request')
 

#Let’s	calculate	the	percentile	values	and	plot	
# them	as	references	in	the	plot	that	has	been generated: 

#3.Calculate	percentile	values	(25th,	50th,75th)	
# for	the	data	to	understand	data distribution 
perc_25	=	np.percentile(y,25) 
perc_50	=	np.percentile(y,50) 
perc_75	=	np.percentile(y,75) 
print 
print	("25th	Percentile				=	%0.2f"%(perc_25)) 
print	("50th	Percentile				=	%0.2f"%(perc_50)) 
print	("75th	Percentile				=	%0.2f"%(perc_75)) 
print   ('')

#4.Plot	these	percentile	values	as	
# reference	in	the	plot	we	generated	
# in	the	previous	step. 

# Draw	horizontal	lines	at	25,50	and	75th	percentile 
plt.axhline(perc_25,label='25th	perc',c='r') 
plt.axhline(perc_50,label='50th	perc',c='g') 
plt.axhline(perc_75,label='75th	perc',c='m')
plt.legend(loc='best') 

# Finally,	let’s	inspect	the	data	
# visually	for	outliers	and	then	
# remove	them	using	the	mask function.	
# Let’s	plot	the	data	again	without	the	outliers:

#5.Look	for	outliers	if	any	in	the	data	
# by	visual	inspection. 

#	Remove	outliers using	mask	function	
#   Remove	outliers 0	and	54
y_masked	=	np.ma.masked_where(y==0,y) 
#		Remove	point	54 
y_masked	=	np.ma.masked_where(y_masked==54,y_masked)

#6	Plot	the	data	again. 
plt.figure(2) 
plt.title("Masked	data") 
plt.plot(x,y_masked,'ro') 
plt.xlabel('year') 
plt.ylabel('No	Presedential	Request') 
plt.ylim(0,60)
plt.show()

#	Draw	horizontal	lines	at	25,50	and	75th	percentile 
plt.axhline(perc_25,label='25th	perc',c='r') 
plt.axhline(perc_50,label='50th	perc',c='g') 
plt.axhline(perc_75,label='75th	perc',c='m') 
plt.legend(loc='best')
plt.show()
