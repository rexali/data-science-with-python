# Let’s	load	the	necessary	libraries.
# 	We	will	follow	it	up	with	
# the	loading	of	our	data	and along	the	way,	
# we	will	handle	the	missing	values.	Finally,	
# we	will	group	the	data	using	a frequency	counter

#	Load	libraries 
import	numpy	as	np 
import	matplotlib.pyplot	as	plt 
from	collections	import	Counter 
from	collections	import	OrderedDict 
from	matplotlib.pylab	import	frange

#	1.Load	the	data	and	handle	missing	values. 
fill_data	=	lambda	x	:	int(x.strip()	or	0) 
data = np.genfromtxt('president.txt',dtype=(int,int),converters= {1:fill_data},delimiter=",") 
x	=	data[:,0] 
y	=	data[:,1]

#	2.Group	data	using	frequency	(count	of	individual	data	points). 
#	Given	a	set	of	points,	Counter()	returns	a	dictionary,	
#   where	key	is	a	data	point, 
#	and	value	is	the	frequency	of	data	point	in	the	dataset. 
x_freq	=	Counter(y) 
x_	=	np.array(x_freq.keys())
y_	=	np.array(x_freq.values())


# We	will	proceed	to	group	the	data	by	the	year	range	
# and	plot	it: 

#	3.Group	data	by	range	of	years 
x_group	=	OrderedDict() 
group=	5 
group_count=1 
keys	=	[] 
values	=	[] 
for	i,xx in	enumerate(x):				
    #	Individual	data	point	is	appended	to	list	keys				
    keys.append(xx)				
    values.append(y[i])				
    #	If	we	have	processed	five	data	points	(i.e.	five	years)				
    if	group_count	==	group:								
    #	Convert	the	list	of	keys	to	a	tuple								
    #	use	the	new	tuple	as	the	ke	to	x_group	dictionary								
        x_group[tuple(keys)]	=	values								
        keys=	[]								
        values	=[]								
        group_count	=	1												
    group_count+=1 
# Accomodate	the	last	batch	of	keys	and	values 
x_group[tuple(keys)]	=	values	
print	(x_group)

#	4.Plot	the	grouped	data	as	dot	plot. 
plt.subplot(311)
plt.title("Dot	Plot	by	Frequency") 
#	Plot	the	frequency 
plt.plot(y_ , x_ , 'ro') 
plt.xlabel('Count') 
plt.ylabel('#	Presedential	Request')

#	Set	the	min	and	max	limits	for	x	axis 
plt.xlim(min(y_)-1,max(y_)+1)
plt.subplot(312) 
plt.title("Simple	dot	plot") 
plt.xlabel('#	Presendtial	Request')
plt.ylabel('Frequency') 

# Finally,	we	will	prepare	the	data	
# for	a	simple	dot	plot	and	proceed	with	
# plotting	it: 

#	Prepare	the	data	for	simple	dot	plot 
#	For	every	(item,	frequency)	pair	create	a	
#	new	x	and	y #	where	x	is	a	list,	
# created	using	using	np.repeat 
#	function,	where	the	item	is	repeated	
# frequency	times. 
#	y	is	a	list	between	0.1	and	frequency/10,	incremented 
#	by	0.1 
for	key,value	in	x_freq.items():				
    x__	=	np.repeat(key,value)				
    y__	=	frange(0.1,(value/10.0),0.1)				
    try:								
        plt.plot(x__,y__,'go')				
    except	ValueError:								
        print	(x__.shape,	y__.shape)				
    #	Set	the	min	and	max	limits	of	x	and	y	axis				
    plt.ylim(0.0,0.4)				
    plt.xlim(xmin=-1)

plt.xticks(x_freq.keys())
plt.subplot(313) 
x_vals	=[] 
x_labels	=[] 
y_vals	=[] 
x_tick	=	1 
for	k,v	in	x_group.items():				
    for	i	in	range(len(k)):								
        x_vals.append(x_tick)								
        x_label	=	'-'.join([str(kk) if	not	i	else str(kk)[-2:]   for	i,kk in	enumerate(k)])								
        x_labels.append(x_label)				
        y_vals.extend(list(v))				
        x_tick+=1
plt.title("Dot	Plot	by	Year	Grouping") 
plt.xlabel('Year	Group') 
plt.ylabel('No	Presedential	Request') 
try:				
    plt.plot(x_vals,y_vals,'ro') 
except	ValueError:				
    print	(len(x_vals),len(y_vals))			
plt.xticks(x_vals,x_labels,rotation=-35)
plt.show()
