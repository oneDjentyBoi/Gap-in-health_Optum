import numpy as np
data=np.genfromtxt('opb1.txt', delimiter=',',dtype='float')
x_fin=[1]*data.shape[0]
#finds the median of a particular parameter and inserts it in the corresponding place with -1 value 
for i in range(0,39):
	x=data[:,i]
	s=[]
	val=0
	for j in range(0,len(x)):
		if x[j]>=0:
			s.append(x[j])
	if len(s)>0:
		val=np.median(s)
	for j in range(0,len(x)):
		if x[j]<0:
			x[j]=val
	x_fin=np.vstack((x_fin,x))
	# print(val)
# x_fin=np.delete(x_fin,[36,37],axis=0)
x_fin=x_fin.T
x_fin=np.unique(x_fin, axis=0)
# print(x_fin.shape)
np.savetxt("opb2.txt",x_fin,delimiter=",")


# finds median for the outcome file and does the same as it did with the data matrix
data=np.genfromtxt('C:\\Users\\USER\\Downloads\\predicting-mortality-of-icu-patients-the-physionet-computing-in-cardiology-challenge-2012-1.0.0\\predicting-mortality-of-icu-patients-the-physionet-computing-in-cardiology-challenge-2012-1.0.0\\Outcomes-b.txt', delimiter=',',dtype='float')
y=[-1]*data.shape[0]
for i in range(1,5):
	y_temp=data[:,i]
	s=[]
	val=0
	for j in range(1,len(y_temp)):
		if float(y_temp[j])>=0:
			s.append(float(y_temp[j]))
		else:
			y_temp[j]=float(y_temp[j])
	if len(s)>0:
		val=np.median(s)
	for j in range(1,len(y_temp)): 
		if float(y_temp[j])<0:
			y_temp[j]=val
	y=np.vstack((y,y_temp))
	print(val)
y=np.vstack((y,data[:,5]))
y=y[1:].T
np.savetxt("opb3.txt",y[1:],delimiter=",") #deletes 1st row, transposes and then deletes 1st row again.