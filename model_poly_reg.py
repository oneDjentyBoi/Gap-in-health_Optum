from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np 
from sklearn.svm import SVC
'''
linear regression
'''
# test_path=
X_b=np.genfromtxt("opb2.txt",delimiter=",") #insert test dataset
X = np.genfromtxt("op2.txt",delimiter=",") #insert training set
data = np.genfromtxt("op3.txt",delimiter=",") #outcome label matrix
y1=[0]*len(X_b)
# print(X_b.shape)
# print(X.shape)

for i in range(0,4):
	y=np.array(data[:,i])
	model = make_pipeline(PolynomialFeatures(2), Ridge()) #polynomial regression with quadratic features 
	model.fit(X, y) #fitting the model with  
	y_predict = model.predict(X_b) #predicting SAP-I, SOFA, length_of_stay and survival
	y1=np.vstack((y1,y_predict))
y1=y1[1:].T
print(y1)#sap,sofa etc.

'''
prediction of whether dead or alive
'''
c1=0
c=0
ans=[0]*len(y1)
y2=data[:,4]
'''
calculates the accuracy of our predictions
'''
for i in range(0,len(y1)):
	if y1[i][2]>=y1[i][3] and y1[i][3]>=0:
		if y2[i]==1:
			c1+=1
		ans[i]=1
	elif y1[i][3]>=0:
		if y2[i]==0:
			c1+=1
	c+=1
ans=np.array([ans])
print("accuracy = ",c1/c)
# percentage of people alive predicted>actual so better caution can be taken.
np.savetxt("opb4.txt",y1,delimiter=",")
