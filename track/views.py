from django.shortcuts import render
from django.http import HttpResponse
from .models import District,Case
import pandas as pd
import json
import os
# Create your views here.




def home(request):
    cases = Case.objects.all()
    description = list()
    
    



    for case in cases:
        description.append(case.description)
        
        

    return render(request,'home.html',{'cases':cases,'total':len(description)})



def stats(request):
    data = pd.read_csv('data/stats.csv')


           





    context = {
        'active':data['Active'][0],
        'cured':data['Discharged'][0],
        'quarantine':data['Quarantined'][0],
        'deaths':data['Deaths'][0],
        'total':data['Total'][0]
        
    }        







    return render(request,'statistics.html',context=context)




def aboutus(request):
    return render(request,'aboutus.html')