# Let’s	proceed	with	seeing	how	we	can	
# invoke	some	machine	learning	
# functionalities	in scikit-learn: 

#Recipe_3b.py 
import	numpy	as	np 
from	sklearn.preprocessing	import	PolynomialFeatures 
#	Data	Preprocessing	routines 
x	=	np.asmatrix([[1,2],[2,4]]) 
poly	=	PolynomialFeatures(degree	=	2) 
poly.fit(x) 
x_poly	=	poly.transform(x) # alternatively,	x_poly	=	poly.fit_transform(x)

print	("Original	x	variable	shape",x.shape)
print   ('') 
print	(x )
print   ('')
print	("Transformed	x	variables",x_poly.shape )
print   ('')
print   (x_poly)
print   ('')

from	sklearn.tree	import	DecisionTreeClassifier 
from	sklearn.datasets	import	load_iris

data	=	load_iris() 
x	=	data['data'] 
y	=	data['target']
estimator	=	DecisionTreeClassifier() 
estimator.fit(x,y) 
predicted_y	=	estimator.predict(x) 
predicted_y_prob	=	estimator.predict_proba(x) 
predicted_y_lprob	=	estimator.predict_log_proba(x)

from	sklearn.pipeline	import	Pipeline

poly	=	PolynomialFeatures(degree=3) 
tree_estimator	=	DecisionTreeClassifier()
steps	=	[('poly',poly),('tree',tree_estimator)] 
estimator	=	Pipeline (steps=steps)
estimator.fit(x,y) 
predicted_y	=	estimator.predict(x)