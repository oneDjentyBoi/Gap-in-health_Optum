# write into a text file the most significant features.

import numpy as np 
scale=100000# to step up the small theta values.
idx={"Age":0,"Height":1,"Weight":2,"Albumin":3,"ALP":4,"ALT":5,"AST":6,
"Bilirubin":7,"BUN":8,"Cholesterol":9,"Creatinine":10,"DiasABP":11,"FiO2":12,
"GCS":13,"Glucose":14,"HCO3":15,"HCT":16,"HR":17,"K":18,
"Lactate":19,"Mg":20,"MAP":21,"MechVent":22,"Na":23,"NIDiasABP":24,
"NIMAP":25,"NISysABP":26,"PaCO2":27,"PaO2":28,"pH":29,"Platelets":30,
"RespRate":31,"SaO2":32,"SysABP":33,"Temp":34,"Tropl":35,"TropT":36,
"Urine":37,"WBC":38}
idx_inv={}
idx_inv[0]="invalid"
for k,v in idx.items():# reversing the idx dictionary
	idx_inv[v+1]=k
def GradDec(x,y,itr,alpha,theta):# normal gradient descent
	m=len(y)
	for _ in range(1,itr):
		h=np.dot(x,theta)
		theta=theta-(alpha/m)*(x.T.dot(h-y))

	return theta
def analytical(x,y):
	theta=np.linalg.inv(x.T.dot(x)).dot(x.T).dot(y)
	return theta

def main():
	x=np.genfromtxt("op2.txt",delimiter=",")
	data=np.genfromtxt("op3.txt",delimiter=",")
	theta=[0]*40
	theta=np.array([theta]).T
	itr=15000
	alpha=0.000001
	for i in range(0,4):
		theta_temp=[0]*40
		theta_temp=np.array([theta_temp]).T
		y=np.array([data[:,i]]).transpose()
		# theta_temp=analytical(x,y)
		theta_temp=GradDec(x,y,itr,alpha,theta_temp)
		theta=np.hstack((theta,theta_temp))

	# theta=analytical(x,y)
	# y=x.dot(theta)
	theta=theta*scale
	priority=[(0,"")]*len(theta)
	for i in range(0,len(theta)):
		priority[i]=(abs(theta[i]).sum(),idx_inv[i])# storing the sum-theta values in a vector
	priority.sort(reverse=True)# sorting the vector in reverse so that we get the most significant parameter on the top
	b2=[]
	b3=[]
	for i in range(len(theta)):
		a,b=priority[i]
		if b!="invalid":
			b2.append(b)	
			b3.append(a)
			print(b)
	file=open("fs.txt","w")
	for i in b2:
		file.write(i)
		file.write('\n')
	file.close()
	np.savetxt("lt.txt",b3,delimiter=",")
	print(priority)
if __name__=="__main__":
	main()
