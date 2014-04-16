from django.shortcuts import render
from django.http import HttpResponse
from branches import get_allBranches
from models import *
import datetime


def add_Country():
    return 
def add_State():
    return 

def add_District():
    return 

def add_City():
    return 

def add_Address():
    return 





def hello(request):
    now = datetime.datetime.now()
    branch_list = get_allBranches('/home/mahaur/ifsc codes/')
    for branch in branch_list:
        branch
    html = "<html><body>Numver of branches is  %s.</body></html>" % str(len(branch_list))
    return HttpResponse(html)
