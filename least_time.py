# take the theta sum values and compute percentage accuracy on that.
import numpy as np
x=np.genfromtxt("C:\\Users\\USER\\Downloads\\predicting-mortality-of-icu-patients-the-physionet-computing-in-cardiology-challenge-2012-1.0.0\\predicting-mortality-of-icu-patients-the-physionet-computing-in-cardiology-challenge-2012-1.0.0\\set-a\\137145.txt",delimiter=",",dtype="str")
y1=np.genfromtxt("lt.txt",delimiter="\n",dtype="float")
y2=np.genfromtxt("fs.txt",delimiter="\n",dtype="str")
total_sum=y1.sum()#sum of all the theta sums.

print("For Patient ID:",int(x[1][2]))

visit=[0]*len(y1)#this has to be maintained so that it does not account for 1 parameter more than twice

dic={}

print(y2)

for i in range(len(y2)):
	dic[y2[i]]=i

par_sum=0

acc=[]

for i in range(2,len(x)):
	if x[i][1]!="Gender" and x[i][1]!="ICUType" and visit[dic[x[i][1]]] == 0:
		par_sum+=y1[dic[x[i][1]]] #whenever a new parameter is encountered, the associated theta-sum value is added in par_sum
		visit[dic[x[i][1]]]=1
		acc.append((par_sum/total_sum,i))
		# print("percent accuracy=",par_sum/total_sum)
d = par_sum/total_sum # percent of total parameters that we have 
t_stamp=0
for i in range(len(acc)):
	a,b=acc[i]
	'''
	predicts How close is the prediction going to be to the maximum achievable accuracy at this time-stamp 
	'''
	stri= "prediction accuracy = %f at time_stamp = %s "%( a/d *100 , x[b][0] ) 
	print(stri)
print("(prediction accuracy = 100 => maximum achievable accuracy)")
