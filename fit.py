import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import datetime
def Rs(f,xdata,ydata,a):
	res = ydata-f(xdata,a)
	ss = np.sum(res**2.0)
	sst = np.sum((ydata-np.mean(ydata))**2.0)
	rs = 1-(ss/sst)
	return rs

dt = datetime.datetime.now()

time = open("time.txt","r")
ccc = open("ccc.txt","r")
cct = open("cct.txt","r")
ctt = open("ctt.txt","r")

Time = []
CCC = []
CCT = []
CTT = []
content = [time.readlines(),ccc.readlines(),cct.readlines(),ctt.readlines()]
for i in range(4):
	for x in content[i]:
        	row = x.split()
		if(i==0):		
			Time.append(float(row[0]))
		elif(i==1):
			CCC.append(float(row[0]))
		elif(i==2):
			CCT.append(float(row[0]))
		elif(i==3):
			CTT.append(float(row[0]))



Time = np.array(Time)
CCC = np.array(CCC)
CCT = np.array(CCT)
CTT = np.array(CTT)

func1 = lambda x,a: CCC[0]*exp(-1*a*x)
func2 = lambda x,a: (CCT[0]-(CCC[0]*(popt[0])/(a-popt[0])))*exp(-1*a*x) + ((CCC[0]*popt[0])/(a-popt[0]))*exp(-1*popt[0]*x)
func3 = lambda x,a: ((CCT[0]-(CCC[0]*(popt[0])/(popt1[0]-popt[0])))*(popt1[0])/(a-popt1[0]))*exp(-1*popt1[0]*x) + (((CCC[0]*popt[0])/(popt1[0]-popt[0]))*(popt1[0])/(a-popt[0]))*exp(-1*popt[0]*x) + (CTT[0] - ((CCT[0]-(CCC[0]*(popt[0])/(popt1[0]-popt[0])))*(popt1[0])/(a-popt1[0])) - (((CCC[0]*popt[0])/(popt1[0]-popt[0]))*(popt1[0])/(a-popt[0])))*exp(-1*a*x)

plt.plot(Time, CCC, 'b.', label='data')
popt, pcov = curve_fit(func1, Time, CCC,p0=[0.0])
plt.plot(Time, func1(Time, *popt), 'r-', label='fit')
rsq = Rs(func1,Time,CCC,popt[0])
print "*******************************"
print "The value of K_0 is: " , popt[0]
print "Covariance is: ",pcov[0][0] 
print "R-Square is: ", rsq
print "*******************************"
plt.xlabel('Time (min)')
plt.ylabel('%CCC')
plt.title("CCC vs Time")
plt.legend()
plt.grid()
ddtt = "CCC_"+dt.strftime("%d-%m-%Y_%H:%M:%S")+".png"
plt.savefig(ddtt)

plt.clf()

plt.plot(Time, CCT, 'b.', label='data')
popt1, pcov1 = curve_fit(func2, Time, CCT,p0=[0.0])
plt.plot(Time, func2(Time, *popt1), 'r-', label='fit')
rsq = Rs(func2,Time,CCT,popt1[0])
print "*******************************"
print "The value of K_1 is: " , popt1[0]
print "Covariance is: ",pcov1[0][0]
print "R-Square is: ", rsq
print "*******************************"
plt.xlabel('Time (min)')
plt.ylabel('%CCT')
plt.title("CCT vs Time")
plt.legend()
plt.grid()
ddtt = "CCT_"+dt.strftime("%d-%m-%Y_%H:%M:%S")+".png"
plt.savefig(ddtt)

plt.clf()

plt.plot(Time, CTT, 'b.', label='data')
popt2, pcov2 = curve_fit(func3, Time, CTT,p0=[0.0])
plt.plot(Time, func3(Time, *popt2), 'r-', label='fit')
rsq = Rs(func2,Time,CTT,popt2[0])
print "*******************************"
print "The value of K_2 is: " , popt2[0]
print "Covariance is: ",pcov2[0][0]
print "R-Square is: ", rsq
print "*******************************"
plt.xlabel('Time (min)')
plt.ylabel('%CTT')
plt.title("CTT vs Time")
plt.legend()
plt.grid()
ddtt = "CTT_"+dt.strftime("%d-%m-%Y_%H:%M:%S")+".png"
plt.savefig(ddtt)


time.close()
cct.close()
ctt.close()
ccc.close()

