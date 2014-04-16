from xlrd import open_workbook
from os import listdir
from os.path import isfile, join

def get_branch(row,header):
	branch ={}	
	i =0
	for head in header:
		if (type(row[i].value) is float):
			branch[head] = "%.0f" % (row[i].value)
		else:
			branch[head] = (row[i].value)
		i = i+1
	return branch

def get_address(branch):
	return branch['Address']


def get_workbook(filename):
	return open_workbook(filename) 

def get_worksheet(workbook,sheetnum):
	sheets = workbook.sheets()
	return sheets[sheetnum] 
def get_header(s):# s is the worksheet
	header = []
	for col in range(s.ncols):
		if (type(s.cell(0,col).value) is float):
			header.append("%.0f" % (s.cell(0,col).value))
		else:
			header.append(s.cell(0,col).value.strip())
	return header
def get_branchesfromfile(filename):
	wb = get_workbook(filename)
	branch_list = []
	for curr_sheet in range(wb.nsheets):
		sheet = get_worksheet(wb,curr_sheet)
		header = get_header(sheet)
		print "Processing",sheet.nrows,"rows"
		
		for curr_row in range(1,sheet.nrows):
			branch = get_branch(sheet.row(curr_row),header)
			branch_list.append(branch)
	return branch_list
def get_xcelfiles(path):
	return [ f for f in listdir(path) if (isfile(join(path,f)) & f.endswith(".xls"))]
def get_allBranches(path):
	files = get_xcelfiles(path)
	branch_list = []
	for filename in files:
		branches = get_branchesfromfile(path+filename)
		branch_list = branch_list + branches
	return branch_list	
#mypath = '/home/mahaur/ifsc codes'
#files = [ f for f in listdir(mypath) if (isfile(join(mypath,f)) & f.endswith(".xls"))]
#i =0
#for filename in files:
#	try:
#		wb = open_workbook(filename)
#		for s in wb.sheets():
#			header = get_header(s)
#			for curr_row in range(1,s.nrows):
#				branch = get_branch(s.row(curr_row),header)
#		print filename + " "+ str(i)
#		i = i+1
#	except:
#		print "Failed "+filename
		
