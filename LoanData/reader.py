import csv
import numpy as np
from numpy import array
from array import *
from numpy import genfromtxt

bvector = []


with open('EqualLoanData.csv') as csvfile:
	readCSV = csv.reader(csvfile,delimiter=',')
	loanAmount = []
	term = []
	empLength = []
	homeStatus = []
	income = []
	purpose = []
	dti = []
	delinq = []
	earliestCredit = []
	ficoLow = []
	ficoHigh = []
	lastInquiry = []
	accounts = []
	pubRec = []
	totalAccounts = []
	lastFicoHigh = []
	lastFicoLow = []
	for row in readCSV:
		a = row[0]
		loanAmount.append(a)
		b = row[1]
		if "36" in b:
			b = 36
		else:
			b = 60
		term.append(b)

		c = row[2]
		if "10+" in c:
			c = 10
		elif "9" in c:
			c = 9
		elif "8" in c:
			c = 8
		elif "7" in c:
			c = 7
		elif "6" in c:
			c = 6
		elif "5" in c:
			c = 5
		elif "4" in c:
			c = 4
		elif "3" in c:
			c = 3
		elif "2" in c:
			c = 2
		elif "1" in c:
			c = 1
		else:
			c = 0
		empLength.append(c)

		d = row[3]
		if "OWN" in d:
			d = 5
		elif "MORTGAGE" in d:
			d = 4
		elif "RENT" in d:
			d = 3
		elif "OTHER" in d:
			d = 2
		else:
			d = 1

		homeStatus.append(d)

		e = row[4]
		income.append(e)

		f = row[5]
		if "wedding" in f:
			f = 1
		elif "vacation" in f:
			f = 2
		elif "small_business" in f:
			f = 3
		elif "renewable_energy" in f:
			f = 4
		elif "moving" in f:
			f = 5
		elif "medical" in f:
			f = 6
		elif "major_purpose" in f:
			f = 7
		elif "house" in f:
			f = 8
		elif "home_improvement" in f:
			f = 9
		elif "education" in f:
			f = 10
		elif "debt_consolidation" in f:
			f = 11
		elif "credit_card" in f:
			f = 12
		elif "car" in f:
			f = 13
		else:
			f = 14
		purpose.append(f)
		g = row[6]
		dti.append(g)
		h = row[7]
		delinq.append(h)
		i = row[8]
		earliestCredit.append(i)
		j = row[9]
		ficoLow.append(j)
		k = row[10]
		ficoHigh.append(k)
		l = row[11]
		lastInquiry.append(l)
		m = row[12]
		accounts.append(m)
		n = row[13]
		pubRec.append(n)
		o = row[14]
		totalAccounts.append(o)
		p = row[15]
		lastFicoLow.append(p)
		q = row[16]
		lastFicoHigh.append(q)
		r = row[17]
		if "Current" in r:
			r = 1
		elif "Fully Paid" in r:
			r = 1
		else:
			r = -1
		bvector.append(r)

Amatrix = np.zeros((len(loanAmount),18))

for i in range(len(loanAmount)):
	Amatrix[i][0]= loanAmount[i]
	Amatrix[i][1]= term[i]
	Amatrix[i][2]=  empLength[i]
	Amatrix[i][3]= homeStatus[i]
	Amatrix[i][4]= income[i]
	Amatrix[i][5]= purpose[i]
	Amatrix[i][6]= dti[i]
	Amatrix[i][7]= delinq[i]
	Amatrix[i][8]= earliestCredit[i]
	Amatrix[i][9]= ficoLow[i]
	Amatrix[i][10]= ficoHigh[i]
	Amatrix[i][11]= lastInquiry[i]
	Amatrix[i][12]= accounts[i]
	Amatrix[i][13]= pubRec[i]
	Amatrix[i][14]= totalAccounts[i]
	Amatrix[i][15]= lastFicoHigh[i]
	Amatrix[i][16]= lastFicoLow[i]
	Amatrix[i][17]= bvector[i]


np.random.shuffle(Amatrix)

for i in range(len(Amatrix)):
	bvector[i] = Amatrix[i][17]

Amatrix = np.delete(Amatrix,17,1)
