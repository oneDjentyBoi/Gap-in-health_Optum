import glob
import os
import numpy as np

# takes the text files all at once

file_list = glob.glob(os.path.join(os.getcwd(), "C:\\Users\\USER\\Downloads\\predicting-mortality-of-icu-patients-the-physionet-computing-in-cardiology-challenge-2012-1.0.0\\predicting-mortality-of-icu-patients-the-physionet-computing-in-cardiology-challenge-2012-1.0.0\\set-b", "*.txt"))

idx={"Age":0,"Height":1,"Weight":2,"Albumin":3,"ALP":4,"ALT":5,"AST":6,
"Bilirubin":7,"BUN":8,"Cholesterol":9,"Creatinine":10,"DiasABP":11,"FiO2":12,
"GCS":13,"Glucose":14,"HCO3":15,"HCT":16,"HR":17,"K":18,
"Lactate":19,"Mg":20,"MAP":21,"MechVent":22,"Na":23,"NIDiasABP":24,
"NIMAP":25,"NISysABP":26,"PaCO2":27,"PaO2":28,"pH":29,"Platelets":30,
"RespRate":31,"SaO2":32,"SysABP":33,"Temp":34,"Tropl":35,"TropT":36,
"Urine":37,"WBC":38}

lookup=[0]*len(file_list)
x_m = [-1]*39 # delete the first row in x_m and x_f
for i in range(0,len(file_list)):
	data = np.genfromtxt(file_list[i],delimiter=",",dtype="str")
	lookup[i] = int(data[1][2]) # patient ID
	x_temp = [-1]*39

	for j in range(2,len(data)):# fills in the data matrix with missing values as -1
		if j!=4:
			for a,b in idx.items():
				if data[j][1]==a:
					x_temp[b]=float(data[j][2])

	x_m=np.vstack((x_m,x_temp))
#saves the data matrix
np.savetxt("opb1.txt",x_m[1:],delimiter=",")

# print(x_m.shape)
# print(x_f.shape)